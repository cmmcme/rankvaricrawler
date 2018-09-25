import sys
sys.path.insert(0, '/src')
from Github.GithubRequester import GithubRequester


class Crawler(object):
    def __init__(self, username, password, language, per_page):
        self.requester = GithubRequester(username, password, per_page)
        self.language = language
        self.per_page = per_page

    def repositories(self):
        results = self.requester.search_repositories(self.language)
        repos = self._get_page_results(results) #
        return repos

    def codes(self, repo_name):
        results = self.requester.search_code(language=self.language, repo=repo_name)
        codes = self._get_page_results(results)
        return codes

    def _get_page_results(self, paginated_list):
        results = []
        length = self._get_page_length(paginated_list.totalCount)
     #   print(length)
        for page in range(0, length):
     #       print(page)
            results += paginated_list.get_page(page) #

        return results

    def _get_page_length(self, total_count):
     #   print(self.per_page, '!!' , total_count)
        if total_count > 1000:
            return (1000 / self.per_page)

        return (total_count / self.per_page)
