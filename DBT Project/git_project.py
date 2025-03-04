import git

# GitHub repository URL
repo_url = "https://github.com/username/repo.git"

# Local path where you want to clone
local_path = r"C:\Users\messe\OneDrive\Desktop"

# Clone the repo
git_project.Repo.clone_from(repo_url, local_path)
print("Repository cloned successfully!")