import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";
import { renderHook, waitFor } from "@testing-library/react";
import { useAuth } from "@/hooks/use-auth";

// Mock dependencies
vi.mock("next/navigation", () => ({
  useRouter: vi.fn(),
}));

vi.mock("@/actions", () => ({
  signIn: vi.fn(),
  signUp: vi.fn(),
}));

vi.mock("@/lib/anon-work-tracker", () => ({
  getAnonWorkData: vi.fn(),
  clearAnonWork: vi.fn(),
}));

vi.mock("@/actions/get-projects", () => ({
  getProjects: vi.fn(),
}));

vi.mock("@/actions/create-project", () => ({
  createProject: vi.fn(),
}));

import { useRouter } from "next/navigation";
import { signIn as signInAction, signUp as signUpAction } from "@/actions";
import { getAnonWorkData, clearAnonWork } from "@/lib/anon-work-tracker";
import { getProjects } from "@/actions/get-projects";
import { createProject } from "@/actions/create-project";

describe("useAuth", () => {
  const mockPush = vi.fn();
  const mockRouter = { push: mockPush };

  beforeEach(() => {
    vi.mocked(useRouter).mockReturnValue(mockRouter as any);
    vi.clearAllMocks();
  });

  afterEach(() => {
    vi.restoreAllMocks();
  });

  describe("initial state", () => {
    it("should return signIn, signUp, and isLoading", () => {
      const { result } = renderHook(() => useAuth());

      expect(result.current).toHaveProperty("signIn");
      expect(result.current).toHaveProperty("signUp");
      expect(result.current).toHaveProperty("isLoading");
      expect(typeof result.current.signIn).toBe("function");
      expect(typeof result.current.signUp).toBe("function");
      expect(typeof result.current.isLoading).toBe("boolean");
    });

    it("should initialize isLoading as false", () => {
      const { result } = renderHook(() => useAuth());

      expect(result.current.isLoading).toBe(false);
    });
  });

  describe("signIn", () => {
    describe("successful sign in", () => {
      it("should handle sign in with anonymous work", async () => {
        const mockAnonWork = {
          messages: [{ role: "user", content: "test message" }],
          fileSystemData: { files: {} },
        };
        const mockProject = { id: "anon-project-123" };

        vi.mocked(signInAction).mockResolvedValue({ success: true });
        vi.mocked(getAnonWorkData).mockReturnValue(mockAnonWork);
        vi.mocked(createProject).mockResolvedValue(mockProject as any);

        const { result } = renderHook(() => useAuth());

        const response = await result.current.signIn("test@example.com", "password123");

        expect(response).toEqual({ success: true });
        expect(signInAction).toHaveBeenCalledWith("test@example.com", "password123");
        expect(getAnonWorkData).toHaveBeenCalled();
        expect(createProject).toHaveBeenCalledWith({
          name: expect.stringContaining("Design from"),
          messages: mockAnonWork.messages,
          data: mockAnonWork.fileSystemData,
        });
        expect(clearAnonWork).toHaveBeenCalled();
        expect(mockPush).toHaveBeenCalledWith("/anon-project-123");
      });

      it("should handle sign in with existing projects", async () => {
        const mockProjects = [
          { id: "project-1", name: "Project 1" },
          { id: "project-2", name: "Project 2" },
        ];

        vi.mocked(signInAction).mockResolvedValue({ success: true });
        vi.mocked(getAnonWorkData).mockReturnValue(null);
        vi.mocked(getProjects).mockResolvedValue(mockProjects as any);

        const { result } = renderHook(() => useAuth());

        const response = await result.current.signIn("test@example.com", "password123");

        expect(response).toEqual({ success: true });
        expect(signInAction).toHaveBeenCalledWith("test@example.com", "password123");
        expect(getAnonWorkData).toHaveBeenCalled();
        expect(getProjects).toHaveBeenCalled();
        expect(mockPush).toHaveBeenCalledWith("/project-1");
        expect(createProject).not.toHaveBeenCalled();
      });

      it("should handle sign in with no projects", async () => {
        const mockNewProject = { id: "new-project-123" };

        vi.mocked(signInAction).mockResolvedValue({ success: true });
        vi.mocked(getAnonWorkData).mockReturnValue(null);
        vi.mocked(getProjects).mockResolvedValue([]);
        vi.mocked(createProject).mockResolvedValue(mockNewProject as any);

        const { result } = renderHook(() => useAuth());

        const response = await result.current.signIn("test@example.com", "password123");

        expect(response).toEqual({ success: true });
        expect(signInAction).toHaveBeenCalledWith("test@example.com", "password123");
        expect(getAnonWorkData).toHaveBeenCalled();
        expect(getProjects).toHaveBeenCalled();
        expect(createProject).toHaveBeenCalledWith({
          name: expect.stringMatching(/New Design #\d+/),
          messages: [],
          data: {},
        });
        expect(mockPush).toHaveBeenCalledWith("/new-project-123");
      });

      it("should not process anon work if messages array is empty", async () => {
        const mockAnonWork = {
          messages: [],
          fileSystemData: { files: {} },
        };
        const mockProjects = [{ id: "project-1", name: "Project 1" }];

        vi.mocked(signInAction).mockResolvedValue({ success: true });
        vi.mocked(getAnonWorkData).mockReturnValue(mockAnonWork);
        vi.mocked(getProjects).mockResolvedValue(mockProjects as any);

        const { result } = renderHook(() => useAuth());

        await result.current.signIn("test@example.com", "password123");

        expect(createProject).not.toHaveBeenCalledWith(
          expect.objectContaining({
            messages: mockAnonWork.messages,
          })
        );
        expect(clearAnonWork).not.toHaveBeenCalled();
        expect(mockPush).toHaveBeenCalledWith("/project-1");
      });
    });

    describe("failed sign in", () => {
      it("should return error result without navigating", async () => {
        const errorResult = { success: false, error: "Invalid credentials" };

        vi.mocked(signInAction).mockResolvedValue(errorResult);

        const { result } = renderHook(() => useAuth());

        const response = await result.current.signIn("test@example.com", "wrongpassword");

        expect(response).toEqual(errorResult);
        expect(signInAction).toHaveBeenCalledWith("test@example.com", "wrongpassword");
        expect(getAnonWorkData).not.toHaveBeenCalled();
        expect(getProjects).not.toHaveBeenCalled();
        expect(createProject).not.toHaveBeenCalled();
        expect(mockPush).not.toHaveBeenCalled();
      });
    });

    describe("loading state", () => {
      it("should set isLoading to true during sign in and false after", async () => {
        vi.mocked(signInAction).mockImplementation(
          () =>
            new Promise((resolve) => {
              setTimeout(() => resolve({ success: true }), 100);
            })
        );
        vi.mocked(getAnonWorkData).mockReturnValue(null);
        vi.mocked(getProjects).mockResolvedValue([{ id: "project-1" }] as any);

        const { result } = renderHook(() => useAuth());

        expect(result.current.isLoading).toBe(false);

        const signInPromise = result.current.signIn("test@example.com", "password123");

        await waitFor(() => {
          expect(result.current.isLoading).toBe(true);
        });

        await signInPromise;

        await waitFor(() => {
          expect(result.current.isLoading).toBe(false);
        });
      });

      it("should set isLoading to false even if sign in fails", async () => {
        vi.mocked(signInAction).mockResolvedValue({
          success: false,
          error: "Network error",
        });

        const { result } = renderHook(() => useAuth());

        await result.current.signIn("test@example.com", "password123");

        expect(result.current.isLoading).toBe(false);
      });

      it("should set isLoading to false even if an exception occurs", async () => {
        vi.mocked(signInAction).mockRejectedValue(new Error("Network failure"));

        const { result } = renderHook(() => useAuth());

        await expect(
          result.current.signIn("test@example.com", "password123")
        ).rejects.toThrow("Network failure");

        expect(result.current.isLoading).toBe(false);
      });
    });
  });

  describe("signUp", () => {
    describe("successful sign up", () => {
      it("should handle sign up with anonymous work", async () => {
        const mockAnonWork = {
          messages: [{ role: "user", content: "test message" }],
          fileSystemData: { files: {} },
        };
        const mockProject = { id: "anon-project-456" };

        vi.mocked(signUpAction).mockResolvedValue({ success: true });
        vi.mocked(getAnonWorkData).mockReturnValue(mockAnonWork);
        vi.mocked(createProject).mockResolvedValue(mockProject as any);

        const { result } = renderHook(() => useAuth());

        const response = await result.current.signUp("new@example.com", "password123");

        expect(response).toEqual({ success: true });
        expect(signUpAction).toHaveBeenCalledWith("new@example.com", "password123");
        expect(getAnonWorkData).toHaveBeenCalled();
        expect(createProject).toHaveBeenCalledWith({
          name: expect.stringContaining("Design from"),
          messages: mockAnonWork.messages,
          data: mockAnonWork.fileSystemData,
        });
        expect(clearAnonWork).toHaveBeenCalled();
        expect(mockPush).toHaveBeenCalledWith("/anon-project-456");
      });

      it("should handle sign up with existing projects", async () => {
        const mockProjects = [
          { id: "project-1", name: "Project 1" },
          { id: "project-2", name: "Project 2" },
        ];

        vi.mocked(signUpAction).mockResolvedValue({ success: true });
        vi.mocked(getAnonWorkData).mockReturnValue(null);
        vi.mocked(getProjects).mockResolvedValue(mockProjects as any);

        const { result } = renderHook(() => useAuth());

        const response = await result.current.signUp("new@example.com", "password123");

        expect(response).toEqual({ success: true });
        expect(signUpAction).toHaveBeenCalledWith("new@example.com", "password123");
        expect(getAnonWorkData).toHaveBeenCalled();
        expect(getProjects).toHaveBeenCalled();
        expect(mockPush).toHaveBeenCalledWith("/project-1");
        expect(createProject).not.toHaveBeenCalled();
      });

      it("should handle sign up with no projects", async () => {
        const mockNewProject = { id: "new-project-789" };

        vi.mocked(signUpAction).mockResolvedValue({ success: true });
        vi.mocked(getAnonWorkData).mockReturnValue(null);
        vi.mocked(getProjects).mockResolvedValue([]);
        vi.mocked(createProject).mockResolvedValue(mockNewProject as any);

        const { result } = renderHook(() => useAuth());

        const response = await result.current.signUp("new@example.com", "password123");

        expect(response).toEqual({ success: true });
        expect(signUpAction).toHaveBeenCalledWith("new@example.com", "password123");
        expect(getAnonWorkData).toHaveBeenCalled();
        expect(getProjects).toHaveBeenCalled();
        expect(createProject).toHaveBeenCalledWith({
          name: expect.stringMatching(/New Design #\d+/),
          messages: [],
          data: {},
        });
        expect(mockPush).toHaveBeenCalledWith("/new-project-789");
      });

      it("should not process anon work if messages array is empty", async () => {
        const mockAnonWork = {
          messages: [],
          fileSystemData: { files: {} },
        };
        const mockProjects = [{ id: "project-1", name: "Project 1" }];

        vi.mocked(signUpAction).mockResolvedValue({ success: true });
        vi.mocked(getAnonWorkData).mockReturnValue(mockAnonWork);
        vi.mocked(getProjects).mockResolvedValue(mockProjects as any);

        const { result } = renderHook(() => useAuth());

        await result.current.signUp("new@example.com", "password123");

        expect(createProject).not.toHaveBeenCalledWith(
          expect.objectContaining({
            messages: mockAnonWork.messages,
          })
        );
        expect(clearAnonWork).not.toHaveBeenCalled();
        expect(mockPush).toHaveBeenCalledWith("/project-1");
      });
    });

    describe("failed sign up", () => {
      it("should return error result without navigating", async () => {
        const errorResult = { success: false, error: "Email already exists" };

        vi.mocked(signUpAction).mockResolvedValue(errorResult);

        const { result } = renderHook(() => useAuth());

        const response = await result.current.signUp("existing@example.com", "password123");

        expect(response).toEqual(errorResult);
        expect(signUpAction).toHaveBeenCalledWith("existing@example.com", "password123");
        expect(getAnonWorkData).not.toHaveBeenCalled();
        expect(getProjects).not.toHaveBeenCalled();
        expect(createProject).not.toHaveBeenCalled();
        expect(mockPush).not.toHaveBeenCalled();
      });
    });

    describe("loading state", () => {
      it("should set isLoading to true during sign up and false after", async () => {
        vi.mocked(signUpAction).mockImplementation(
          () =>
            new Promise((resolve) => {
              setTimeout(() => resolve({ success: true }), 100);
            })
        );
        vi.mocked(getAnonWorkData).mockReturnValue(null);
        vi.mocked(getProjects).mockResolvedValue([{ id: "project-1" }] as any);

        const { result } = renderHook(() => useAuth());

        expect(result.current.isLoading).toBe(false);

        const signUpPromise = result.current.signUp("new@example.com", "password123");

        await waitFor(() => {
          expect(result.current.isLoading).toBe(true);
        });

        await signUpPromise;

        await waitFor(() => {
          expect(result.current.isLoading).toBe(false);
        });
      });

      it("should set isLoading to false even if sign up fails", async () => {
        vi.mocked(signUpAction).mockResolvedValue({
          success: false,
          error: "Validation error",
        });

        const { result } = renderHook(() => useAuth());

        await result.current.signUp("invalid@example.com", "123");

        expect(result.current.isLoading).toBe(false);
      });

      it("should set isLoading to false even if an exception occurs", async () => {
        vi.mocked(signUpAction).mockRejectedValue(new Error("Database connection failed"));

        const { result } = renderHook(() => useAuth());

        await expect(
          result.current.signUp("new@example.com", "password123")
        ).rejects.toThrow("Database connection failed");

        expect(result.current.isLoading).toBe(false);
      });
    });
  });

  describe("edge cases", () => {
    it("should handle undefined anon work", async () => {
      const mockProjects = [{ id: "project-1", name: "Project 1" }];

      vi.mocked(signInAction).mockResolvedValue({ success: true });
      vi.mocked(getAnonWorkData).mockReturnValue(undefined as any);
      vi.mocked(getProjects).mockResolvedValue(mockProjects as any);

      const { result } = renderHook(() => useAuth());

      await result.current.signIn("test@example.com", "password123");

      expect(createProject).not.toHaveBeenCalledWith(
        expect.objectContaining({
          messages: expect.anything(),
        })
      );
      expect(clearAnonWork).not.toHaveBeenCalled();
      expect(mockPush).toHaveBeenCalledWith("/project-1");
    });

    it("should handle empty projects array correctly", async () => {
      const mockNewProject = { id: "fallback-project" };

      vi.mocked(signInAction).mockResolvedValue({ success: true });
      vi.mocked(getAnonWorkData).mockReturnValue(null);
      vi.mocked(getProjects).mockResolvedValue([]);
      vi.mocked(createProject).mockResolvedValue(mockNewProject as any);

      const { result } = renderHook(() => useAuth());

      await result.current.signIn("test@example.com", "password123");

      expect(createProject).toHaveBeenCalled();
      expect(mockPush).toHaveBeenCalledWith("/fallback-project");
    });

    it("should navigate to most recent project when multiple exist", async () => {
      const mockProjects = [
        { id: "project-newest", name: "Newest" },
        { id: "project-older", name: "Older" },
        { id: "project-oldest", name: "Oldest" },
      ];

      vi.mocked(signInAction).mockResolvedValue({ success: true });
      vi.mocked(getAnonWorkData).mockReturnValue(null);
      vi.mocked(getProjects).mockResolvedValue(mockProjects as any);

      const { result } = renderHook(() => useAuth());

      await result.current.signIn("test@example.com", "password123");

      expect(mockPush).toHaveBeenCalledWith("/project-newest");
    });

    it("should generate different random project names", async () => {
      vi.mocked(signInAction).mockResolvedValue({ success: true });
      vi.mocked(getAnonWorkData).mockReturnValue(null);
      vi.mocked(getProjects).mockResolvedValue([]);
      vi.mocked(createProject).mockResolvedValue({ id: "test" } as any);

      const { result } = renderHook(() => useAuth());

      await result.current.signIn("test@example.com", "password123");

      expect(createProject).toHaveBeenCalledWith({
        name: expect.stringMatching(/^New Design #\d+$/),
        messages: [],
        data: {},
      });

      const firstCallName = vi.mocked(createProject).mock.calls[0][0].name;
      expect(firstCallName).toMatch(/^New Design #\d+$/);
    });
  });
});
