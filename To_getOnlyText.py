from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# url = "https://www.simplicant.com/blog/"
url="https://www.simplicant.com/company/contact/"
html = urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

# print(text)

# url = "https://www.freshworks.com/hrms/free-applicant-tracking-system/"
EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# initiate an HTTP session
# session = HTMLSession()

# get the HTTP Response
# r = session.get(url)

# # for JAVA-Script driven websites
# r.html.render()

for re_match in re.finditer(EMAIL_REGEX, text):
    print((re_match.group()))
    if ((re_match.group())) == 0:
        print("H---")
    else:
        print("NO")
    print(re.finditer(EMAIL_REGEX, text))