# create temp workspace
# clone repo
# return local path
# cleanup later


from pathlib import Path              #safe filesystem path handling
import tempfile                      #create temporary directories safely ,unique folder created ,avoids:naming collisions,overwriting,manual management
from git import Repo
import json
import os
from app.core.config import settings
import stat
import shutil
import os


def remove_readonly(func, path, _):
        os.chmod(path, stat.S_IWRITE)
        func(path)


class RepoManager:
    def __init__(self):
        self.current_repo_path = None

    def clone_repository(self, repo_url: str):
        repo_path = Path(settings.REPO_STORAGE_PATH)
        
        if repo_path.exists():
            shutil.rmtree(repo_path, onerror=remove_readonly)
        
        repo_path.mkdir(parents=True, exist_ok=True)
        Repo.clone_from(repo_url, repo_path)
        self.current_repo_path = repo_path
        return repo_path

    def get_repo_path(self):
        return self.current_repo_path
    
   

    def save_repo_path(self):
        with open(settings.REPO_PATH_FILE, "w") as f:
            json.dump({"repo_path": str(self.current_repo_path)}, f)

    def load_repo_path(self):
        if os.path.exists(settings.REPO_PATH_FILE):
            with open(settings.REPO_PATH_FILE, "r") as f:
                data = json.load(f)
                self.current_repo_path = Path(data["repo_path"])
            print("Repo path loaded from disk")

repo_manager = RepoManager()

