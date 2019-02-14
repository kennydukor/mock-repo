# Contributions-Importer-For-Github/run_script.py
import git
from git_contributions_importer import *

# Your private repo or Bitbucket repo
repo = git.Repo("C:\WAPXCONNECT\middleware")
# Your mock repo
mock_repo = git.Repo("C:\WAPXCONNECT\mock-repo")
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_author(['kennydukor@gmail.com', '32472950+kennydukor@users.noreply.github.com'])
importer.import_repository()
