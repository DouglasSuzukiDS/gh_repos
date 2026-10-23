import subprocess

repos = [
   'repo1',
   'repo2',
   'repo3',
]

gh_user_origin = 'GH_USER_ORIGIN'
correct_name = 'YOUR_GITHUB_USER'
correct_email = 'YOUR_EMAIL_GITHUB_ACCOUNT'

for repo in repos:
   bare_repo = f'{repo}.git'
   
   subprocess.run(['git', 'clone', '--bare', f'https://github.com/{gh_user_origin}/{repo}.git'], check=True)
   
   # Força a alteração em absolutamente todos os commits
   filter_script = f'''
   export GIT_COMMITTER_NAME='{correct_name}'
   export GIT_COMMITTER_EMAIL='{correct_email}'
   export GIT_AUTHOR_NAME='{correct_name}'
   export GIT_AUTHOR_EMAIL='{correct_email}'
   '''
   
   subprocess.run(['git', '-C', bare_repo, 'filter-branch', '--env-filter', filter_script, '--tag-name-filter', 'cat', '--', '--all'], check=True)
    
   subprocess.run(['git', '-C', bare_repo, 'update-ref', '-d', 'refs/original/refs/heads/master'], check=True)
   subprocess.run(['git', '-C', bare_repo, 'update-ref', '-d', 'refs/original/refs/heads/main'], check=True)
   
   subprocess.run(['git', '-C', bare_repo, 'reflog', 'expire', '--expire=now', '--all'], check=True)
   subprocess.run(['git', '-C', bare_repo, 'gc', '--prune=now', '--aggressive'], check=True)
   
   subprocess.run(['git', '-C', bare_repo, 'remote', 'set-url', 'origin', f'https://github.com/{correct_name}/{repo}.git'], check=True)
   subprocess.run(['git', '-C', bare_repo, 'push', '-u', 'origin', '--all', '--force'], check=True)
   subprocess.run(['git', '-C', bare_repo, 'push', 'origin', '--force', '--tags'], check=True)