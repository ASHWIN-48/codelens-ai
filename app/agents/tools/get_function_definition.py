from langchain_core.tools import tool
from app.utils.repo_manager import repo_manager

@tool
def get_function_definition(file_path: str, function_name: str):
    """
    Extract a specific function or class definition from a file.
    Use this when you know exactly which function you need to inspect.
    """
    file_path = file_path.lstrip("/\\")
    full_path = repo_manager.get_repo_path() / file_path

    if not full_path.exists():
        return f"File not found: {file_path}"

    lines = full_path.read_text(encoding="utf-8", errors="ignore").splitlines()

    result = []
    inside = False
    indent_level = None

    for line in lines:
        if f"def {function_name}" in line or f"class {function_name}" in line:
            inside = True
            indent_level = len(line) - len(line.lstrip())
            result.append(line)
            continue

        if inside:
            if line.strip() == "":
                result.append(line)
                continue
            current_indent = len(line) - len(line.lstrip())
            if current_indent <= indent_level and line.strip():
                break
            result.append(line)

    if not result:
        return f"Function or class '{function_name}' not found in {file_path}"

    return "\n".join(result)