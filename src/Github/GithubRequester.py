from github import Github


class GithubRequester(object):
    def __init__(self, username, password):
        self.g = Github(username, password, per_page=100)

    def search_repositories(self, language):
        q = 'topic:' + language
        return self.g.search_repositories(query=q, sort='stars', order='desc')