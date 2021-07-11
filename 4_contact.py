from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import webbrowser
from requests_html import HTMLSession
# pip3 install requests-html
url = urlopen("https://www.simplicant.com/company/contact/")
bsobj = BeautifulSoup(url,"lxml")
# print(bsobj)
# webbrowser.open_new_tab("https://www.google.com/")
url = "https://www.simplicant.com/company/contact/"
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# initiate an HTTP session
session = HTMLSession()

# get the HTTP Response
r = session.get(url)

# # for JAVA-Script driven websites
# r.html.render()

for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
    print(tuple(re_match.group()))
    if len(tuple(re_match.group())) ==0:
        print("H---")
    else:
        print("NO")

