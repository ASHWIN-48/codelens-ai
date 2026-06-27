from pathlib import Path
class FileLoader:
    IGNORED_DIRS = {
    ".git",
    "node_modules",
    "venv",
    "__pycache__",
    "dist",
    "build"
}
    ALLOWED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".md",
    ".json"
}
        
    def load_repository_files(self, repo_path: Path):
        files = []
        for file_path in repo_path.rglob("*"):
            if any(part in self.IGNORED_DIRS for part in file_path.parts):
                continue
            if file_path.is_file():
                document = self.extract_file_content(file_path, repo_path)
                if document:
                    files.append(document)
        return files

    def extract_file_content(self, file_path: Path, repo_path: Path):
        try:
            content = file_path.read_text(encoding="utf-8")
            return {
                "path": str(file_path.relative_to(repo_path)),
                "extension": file_path.suffix,
                "content": content
            }
        except UnicodeDecodeError:
            return None
         
    