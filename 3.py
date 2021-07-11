from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import webbrowser
from requests_html import HTMLSession


try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "allintext: blog Applicant Tracking System"
pages =set()
# with open("1.html","w") as f:
#      f.write("\n")
for j in search(query, tld="co.in",lang='en', start=0,num=10, stop=5, pause=1): 
    with open("1.html","a") as f:
    #  f.write(j+"\n")
     pages.add(j)
    # print(j+"\n") 
# f.close()
# print(len(pages))

# print(pages)

# ########################

# pip3 install requests-html
# url = urlopen("https://www.simplicant.com/company/contact/")
# bsobj = BeautifulSoup(url,"lxml")
# print(bsobj)
# webbrowser.open_new_tab("https://www.google.com/")
for i in pages:
    #  url = "https://www.simplicant.com/company/contact/"
    EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
     # initiate an HTTP session
    session = HTMLSession()

     # get the HTTP Response
    r = session.get(i)

    # for JAVA-Script driven websites
    # r.html.render()
    print(i)
    # email = []
    for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
     print(re_match.group)
    #    email.append(re_match)
    #    print(email[0])
    print("-----------------------")
  
  