import requests
from bs4 import BeautifulSoup as BS

URL = "https://paikat.te-palvelut.fi/tpt/?searchPhrase=python&locations=Uusimaa&announced=3&leasing=0&english=false&sort=1"
URL ="https://tyopaikat.oikotie.fi/tyopaikat/uusimaa?hakusana=python"

"stripped-ul"
headerList = [
    {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8"
    },
    {
        "User-Agent": "Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0",
        "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.8"
    }
]
response = requests.get(URL, headerList[0])
if response.status_code == 200:
    soup = BS(response.text, "html.parser")
    container = soup.find("ul", attrs={"class": "stripped-ul"})
    test = container.find_all("li", attrs={"class": "stripped-li"})
print(test)

"""Need to install Selenium"""