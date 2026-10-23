from github import Github

# GitHub Access Token
token = "ggrgrgrgrg"
g = Github(token)

for repo in g.get_user().get_repos(type="owner"):
   if not repo.private:
      repo.edit(private=True) # Private
      print(f"Repositório tornado privado: {repo.name}")