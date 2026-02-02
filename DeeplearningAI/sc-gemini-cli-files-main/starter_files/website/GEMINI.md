## Project Overview

This is a web application for a technology conference called "TechStack Conference". It's built using React, TypeScript, and Vite. The project uses Tailwind CSS for styling and Vitest for testing. The application features several pages, including a home page, a session catalog, session details, registration, and other conference-related information. It uses `react-router-dom` for routing and lazy loading for performance optimization.

## Building and Running

### Available Scripts

You can use the following npm scripts to work with this project:

-   `npm run dev`: Starts the development server with Hot Module Replacement (HMR).
-   `npm run build`: Builds the application for production.
-   `npm run lint`: Lints the codebase using ESLint.
-   `npm run test`: Runs the tests using Vitest.
-   `npm run preview`: Serves the production build locally for preview.
-   `npm run preflight`: A utility script that runs linting, testing, and building in sequence.

### Development

To start the development server, run:

```bash
npm run dev
```

### Testing

To run the tests, run:

```bash
npm run test
```

## Development Conventions

### Code Style

The project uses ESLint for code linting. The configuration can be found in `eslint.config.js`. It's recommended to run `npm run lint` periodically to check for code style issues.

### Testing

Tests are written using Vitest and React Testing Library. Test files are co-located with the components they test (e.g., `src/components/Layout.test.tsx`). The test environment is configured in `vite.config.ts` to use `jsdom`.

### Git

The `.gitignore` file is configured to exclude common development artifacts, such as `node_modules` and `dist`.
