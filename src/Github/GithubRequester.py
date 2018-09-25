from github import Github


class GithubRequester(object):
    def __init__(self, username, password, per_page):
        self.g = Github(username, password, per_page=per_page)

    def search_repositories(self, language):
        query= 'topic:' + language
        return self.g.search_repositories(query=query, sort='stars', order='desc')

    def search_code(self, language, repo):
        query = 'language:' + language
        return self.g.search_code(query=query, repo=repo)
