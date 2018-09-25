import getpass
from Github.GithubRequester import GithubRequester

username = raw_input("Username: ")
password = getpass.getpass("Password: ")

github_requester = GithubRequester(username, password)
results = github_requester.search_repositories(language='java')


for page in range(0, 9):
    repos = results.get_page(page)
    for repo in repos:
        print(repo)