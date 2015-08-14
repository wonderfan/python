from bs4 import BeautifulSoup
soup = BeautifulSoup(open("index.html"))
soup = BeautifulSoup(html_doc, 'html.parser')

BeautifulSoup(markup, "lxml") #use different html parser
BeautifulSoup(markup, "html5lib")

for link in soup.find_all('a'):
    print(link.get('href'))

for result in soup.select("a.menu"):
    print(result.get('href'))
