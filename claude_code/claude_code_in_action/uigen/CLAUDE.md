# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

UIGen is an AI-powered React component generator with live preview. It uses Claude AI to generate React components, which are stored in a virtual file system and previewed in real-time using Babel transformation and import maps.

## Prerequisites

- Node.js 18+
- npm

## Environment Setup

Create a `.env` file in the project root (optional):

```env
ANTHROPIC_API_KEY=your-api-key-here
```

If `ANTHROPIC_API_KEY` is not set, the app uses a mock provider that returns static code instead of calling the Claude API. This allows development without an API key.

## Development Commands

### Initial Setup
```bash
npm run setup  # Install dependencies + generate Prisma client + run migrations
```

### Development
```bash
npm run dev           # Start dev server with turbopack (requires node-compat.cjs)
npm run dev:daemon    # Start dev server in background, logs to logs.txt
```

### Testing
```bash
npm run test                    # Run all tests
npm run test -- <pattern>       # Run tests matching pattern (e.g., file-system)
npm run test -- --watch         # Run tests in watch mode
```

### Database
```bash
npx prisma generate              # Regenerate Prisma client
npx prisma migrate dev           # Create and apply migrations
npm run db:reset                 # Reset database (force)
npx prisma studio                # Open Prisma Studio
```

### Build & Deploy
```bash
npm run build         # Production build
npm run start         # Start production server
npm run lint          # Run ESLint
```

## Architecture

### Virtual File System

The core abstraction is `VirtualFileSystem` (src/lib/file-system.ts), which stores files in memory rather than on disk:

- Files are stored as `FileNode` objects in a Map structure
- Supports standard operations: create, read, update, delete, rename
- Serializes to/from JSON for database persistence
- Powers both the code editor and live preview
- Text editor-like operations: `viewFile`, `replaceInFile`, `insertInFile`

**Key insight**: All file operations work with this virtual file system, not the actual filesystem. When debugging file issues, check the VirtualFileSystem state, not disk.

### AI Integration Flow

1. **Chat API** (src/app/api/chat/route.ts):
   - Receives messages and serialized file system state
   - Reconstructs VirtualFileSystem from serialized data
   - Uses Vercel AI SDK's `streamText` with Claude
   - Provides two tools to the AI:
     - `str_replace_editor`: Find/replace operations in files
     - `file_manager`: Rename or delete files/folders
   - On completion, serializes file system back to database

2. **AI Prompt** (src/lib/prompts/generation.tsx):
   - System prompt that instructs Claude how to generate components
   - Cached using Anthropic's prompt caching (`cacheControl: { type: "ephemeral" }`)

3. **Mock Provider** (src/lib/provider.ts):
   - When `ANTHROPIC_API_KEY` is not set, uses mock provider that returns static code
   - Real provider uses `@ai-sdk/anthropic` with Claude Sonnet 4

### JSX Transformation & Preview

The preview system (src/lib/transform/jsx-transformer.ts) transforms code into executable HTML:

1. **Transform Phase**:
   - Uses `@babel/standalone` to transform JSX/TSX → JavaScript
   - Detects and separates CSS imports
   - Creates Blob URLs for transformed code
   - Handles TypeScript by applying both React and TypeScript presets

2. **Import Map Creation** (`createImportMap`):
   - Maps third-party packages to esm.sh CDN (e.g., `react` → `https://esm.sh/react@19`)
   - Maps local files to their Blob URLs
   - Supports `@/` alias (maps to root directory)
   - Creates placeholder modules for missing imports
   - Collects all CSS into a single styles string

3. **Preview HTML** (`createPreviewHTML`):
   - Generates complete HTML document with Tailwind CDN
   - Embeds import map as `<script type="importmap">`
   - Shows syntax errors prominently if transforms failed
   - Wraps app in React ErrorBoundary
   - Dynamically imports entry point and renders to `#root`

**Important**: Syntax errors in any file prevent preview from loading. The preview HTML shows a styled error report instead of rendering the app.

### React Context Architecture

Two main contexts manage application state:

1. **FileSystemContext** (src/lib/contexts/file-system-context.tsx):
   - Wraps VirtualFileSystem with React state
   - Provides file operations: create, update, delete, rename
   - Handles AI tool calls (updates file system based on AI actions)
   - Triggers re-renders via `refreshTrigger` counter

2. **ChatContext** (src/lib/contexts/chat-context.tsx):
   - Manages chat messages and AI streaming
   - Uses Vercel AI SDK's `useChat` hook
   - Sends file system state with each message
   - Updates file system based on AI tool calls

### Database Schema

**Reference the schema file**: Always check `prisma/schema.prisma` to understand the structure of data stored in the database.

Prisma schema (prisma/schema.prisma):

- **User**: email, password (bcrypt hashed), projects relationship
- **Project**: name, userId (nullable for anonymous), messages (JSON array), data (serialized VirtualFileSystem), timestamps
- Prisma client generated to custom location: `src/generated/prisma`

Anonymous users can create projects without accounts (userId is null). Projects are persisted only for authenticated users.

### Authentication

JWT-based auth (src/lib/auth.ts):

- Sign up/sign in with email and password (bcrypt)
- JWT stored in cookies (using `jose` library)
- Middleware (src/middleware.ts) protects routes
- Hook: `useAuth` (src/hooks/use-auth.ts)

### Project Structure

```
src/
├── actions/          # Server actions (create/get projects)
├── app/              # Next.js 15 App Router
│   ├── api/chat/     # AI chat endpoint
│   └── [projectId]/  # Dynamic project page
├── components/
│   ├── auth/         # Auth dialogs and forms
│   ├── chat/         # Chat interface, message list, input
│   ├── editor/       # Code editor (Monaco), file tree
│   ├── preview/      # Preview iframe
│   └── ui/           # Radix UI components
├── lib/
│   ├── contexts/     # React contexts (file-system, chat)
│   ├── tools/        # AI tools (str-replace, file-manager)
│   ├── transform/    # JSX transformer and import map
│   └── prompts/      # AI system prompts
└── generated/prisma/ # Generated Prisma client
```

## Important Development Notes

### Code Style

Use comments sparingly. Only comment complex code where the logic isn't self-evident.

### Node Compatibility

The project requires `node-compat.cjs` to be loaded via `NODE_OPTIONS='--require ./node-compat.cjs'`. This is already configured in all npm scripts.

**Why**: Node.js 25+ exposes global `localStorage`/`sessionStorage` via the experimental Web Storage API. Without `--localstorage-file`, these globals exist but are non-functional, causing "localStorage.getItem is not a function" errors during SSR when dependencies detect the global and assume a browser environment. The compatibility script removes these globals on the server to restore pre-25 behavior where SSR guard checks work correctly.

### Prisma Custom Output

Prisma client is generated to `src/generated/prisma` (not default `node_modules/.prisma/client`). Always import from `@/generated/prisma` or use the wrapper at `src/lib/prisma.ts`.

### Testing

Tests use Vitest with jsdom environment:
- File system tests: `src/lib/__tests__/file-system.test.ts`
- Transform tests: `src/lib/transform/__tests__/jsx-transformer.test.ts`
- Context tests: `src/lib/contexts/__tests__/`
- Component tests: `src/components/*/__tests__/`

### AI Behavior

When the AI generates or modifies files:
1. It receives the full VirtualFileSystem state as serialized JSON
2. It uses `str_replace_editor` tool for content changes
3. It uses `file_manager` tool for rename/delete operations
4. Changes are persisted to database on chat completion (for authenticated users)

The AI is limited to `maxSteps: 40` (or 4 for mock provider) to prevent infinite loops.

### Preview Debugging

If preview doesn't load:
1. Check browser console for import errors
2. Verify all imported files exist in VirtualFileSystem
3. Check for syntax errors in transform phase (shown in preview UI)
4. Verify import map includes all necessary packages
5. Check that entry point has a default export

The preview uses import maps, which require a modern browser with import map support.
