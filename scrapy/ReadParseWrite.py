from bs4 import BeautifulSoup

orig_file = "main.html"
temp_file = "temp.html"

soup = BeautifulSoup(open(orig_file),'html.parser')

body = soup.find("body")

'''
scripts = body.find_all("script")
for js in scripts:
    js.extract()

styles = body.find_all("style")
for css in styles:
    css.extract()
'''

target_div = body.select_one("div.frame")

content = target_div.prettify("utf-8")
with open(temp_file, "wb") as file:
    file.write(content)
