from bs4 import BeautifulSoup
import requests

url = 'https://www.google.com/search?q=how+to+fixe+metadata+automatically+on+alfresco&sxsrf=APq-WBsSZHHf71rUMIRAi2Hd9EKw1hNCDg%3A1643387296437&ei=oBn0YdGIGoyoa9nmt5gB&ved=0ahUKEwjR2KDg7tT1AhUM1BoKHVnzDRMQ4dUDCA4&oq=how+to+fixe+metadata+automatically+on+alfresco&gs_lcp=Cgdnd3Mtd2l6EAw6BgizARCFBDoGCC4QChBDOgQIABBDOgsILhCABBCxAxCDAToFCAAQgARKBAhBGABKBAhGGABQqQxY_G1grHhoAnAAeACAAfUBiAGwA5IBBTAuMS4xmAEAoAEBoAECsAEBwAEB&sclient=gws-wiz'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
span = soup.find('span', id = "error-message")
print(span)

