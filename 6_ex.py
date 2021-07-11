from bs4 import BeautifulSoup 
import requests,re
from urllib.request import urlopen
# import urlparse, urllib

# :::::::::::::Search for ankel tag's attributes which have text == Contact regx :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

email_id = re.compile(r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])""")
# html =urlopen("https://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python")
html =urlopen("https://dir.indiamart.com/nagpur/gym-equipments.html")
soup = BeautifulSoup(html,'lxml')
emails = soup.find_all(text = email_id)
if len(emails) > 0:
    #  print(len(emails))
    for email  in emails:
     print((email))
else:
    print("There is no email id on Home page")
    # soup.find_all(text="Contact")
    # for 'href' in contact.attrs:
    #     print(contact)
    # if soup.find_all(text=re.compile("^(Contact)+")):
    #    if 'href' in link.attrs:
    for link in soup.findAll('a'):
              if link.contents ==soup.find_all(text=re.compile("^(Contact)+")):
                # print(link.contents)
                print (link.attrs['href'])
                html1 = urlopen(link.attrs['href'])
                soup = BeautifulSoup(html1,'lxml')
                emails = soup.find_all(text = email_id)
                if len(emails) > 0:
                 #  print(len(emails))
                   for email  in emails:
                     print((email))
                else:
                  print("There is no email id on Contact page")
        # for link in soup.body.find(text=re.compile("^(Contact)+")).parent:
            # if 'href' in link.attrs:
            #  print(link.content)
                # item =  urlparse.urlparse(link['href'].lower())
                # print(item)
    #      print(link.attrs['href'])

