import csv

f = csv.writer(open("test.csv", "w"))
f.writerow(["Name", "Link"])  

links = soup.find_all('a')
for link in links:
    names = link.contents[0]
    fullLink = link.get('href')

    f.writerow([names,fullLink])
