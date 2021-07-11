# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re


# html = urlopen(re.compile("^(https://www.google.com/).(blog)*"))
# print(html)
# # bsobj = BeautifulSoup(html,"lxml")
# # filename="1.html"
# # # html =urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
# # # bsobj= BeautifulSoup(html,"lxml")
# # bs =bsobj.getText()
# # # with open(filename,"w") as f:
# # #     f.write(bs)
# # print(bs)


try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
  
# to search 
query = "The electric field E between drain and source is decreased with"
pages =set()
with open("1.html","w") as f:
     f.write("\n")
for j in search(query, tld="co.in",lang='en', start=0,num=10, stop=10, pause=2): 
    with open("1.html","a") as f:
     f.write(j+"\n")
     pages.add(j)
    # print(j+"\n") 
f.close()
# print(len(pages))
print(pages)