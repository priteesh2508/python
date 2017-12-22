from bs4 import BeautifulSoup

f=open("blog-front.html","r")
html_doc = f.read()
#print(html_doc)
tgct={}

def parse(tag, lvl):
    if tag is None:
        return
    if tag.name in tgct:
        tgct[tag.name].append(lvl);
    else:
        tgct[tag.name]=[lvl]
    for j in tag.find_all(True, recursive=False):
        parse(j,lvl+1)
    
soup = BeautifulSoup(html_doc, "lxml")
headtag = soup.head
bodytag = soup.body
tgct["html"]=[1]
tgct["body"]=[2]
tgct["head"]=[2]
for j in headtag.find_all(True, recursive=False):
    parse(j,3)
for j in bodytag.find_all(True, recursive=False):
    parse(j,3)
    
print(tgct)
       