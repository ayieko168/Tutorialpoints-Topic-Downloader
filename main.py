import urllib.request, urllib.error, urllib.parse
from bs4 import BeautifulSoup
import os

url = "https://www.tutorialspoint.com/pyqt/index.htm"

hdr = {"User-Agent": "Mozila/5.0"}
req = urllib.request.Request(url, headers=hdr)
page = urllib.request.urlopen(req)
soup = BeautifulSoup(page, "html.parser")

luElement = soup.find("ul", {"class": "toc chapters"})
liElements = luElement.find_all("li")

try:
    DIR = os.getcwd()
    os.makedirs("{}\\pyqt".format(DIR))
except:
    pass
for item in liElements:

    try:
        link = item.find("a").get("href")
        linkName = str(link.split("/")[-1]) + "l"

        print("link = ", linkName)
        
        url = 'https://www.tutorialspoint.com/{}'.format(link)
        print("url = ", url)

        response = urllib.request.urlopen(url)
        webContent = response.read().decode("utf-8")
        
        dest = "{}\\pyqt\\{}".format(DIR, linkName)
        print("dest = ", dest)
        f = open(dest, 'w')
        f.write(webContent)
        f.close


    except Exception as e:
        print("Exception :: ", e)
    
    
