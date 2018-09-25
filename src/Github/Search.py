import requests
from GithubRequester import GithubRequester


class Search(GithubRequester):
    def __init__(self):
        GithubRequester.__init__(self)
        self.path = '/search'

    def repositories(self, language, page=1, per_page=30):
        query = 'q=topic:' +  language + '&sort=stars&order=desc&per_page=' + str(per_page) + '&page=' + str(page)
        url = self.generateURL(self.path + '/repositories', query)
        return requests.get(url).json()

    def code(self, language, user, repo):
        query = 'q=language:' + language + '+repo:' + user + '/' + repo
        url = self.generateURL(self.path + '/code', query)
        return requests.get(url).json()