import getpass
import requests
from Crawler.Crawler import Crawler

LANGUAGE = 'java'
PER_PAGE = 100
RAW_URL = 'https://raw.githubusercontent.com/'
username = raw_input("Username: ")
password = getpass.getpass("Password: ")

crawler = Crawler(username=username, password=password, language=LANGUAGE, per_page=PER_PAGE)
repos = crawler.repositories()
##print(len(repos))
##print (repos[0].default_branch)
##codes = crawler.codes(repos[0].full_name)
##print(codes[0])

for re in repos:
    default_branch = re.default_branch
    codes = crawler.codes(re.full_name)
    for code in codes:
        paths = RAW_URL + re.full_name + '/' + default_branch +  '/' + code.path
        requests.post('http://localhost:5000/user', json={'url' : paths, 'language' : LANGUAGE})
        print(paths)