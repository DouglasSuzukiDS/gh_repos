import subprocess

repos = [
   'repo1',
   'repo2',
]

user = 'GH_USER'  # Replace with your GitHub username

for repo in repos:
   repo_name = repo.split()[0]

   url = f"https://github.com/{user}/{repo_name}.git"

   print(f"Cloning {repo_name}...")

   subprocess.run(["git", "clone", url])