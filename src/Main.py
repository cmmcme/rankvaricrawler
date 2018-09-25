import getpass
from Crawler.Crawler import Crawler

LANGUAGE = 'java'
PER_PAGE = 100

username = raw_input("Username: ")
password = getpass.getpass("Password: ")

crawler = Crawler(username=username, password=password, language=LANGUAGE, per_page=PER_PAGE)
repos = crawler.repositories()
print(len(repos))
print (repos[0].default_branch)
codes = crawler.codes(repos[0].full_name)
print(codes[0])