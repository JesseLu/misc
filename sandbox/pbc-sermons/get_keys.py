import re
import urllib2

text = open("raw_archive.txt").read()
titles = re.findall(r'<Key>(.*?)</Key>', text, re.DOTALL)
f = open("links.txt", "w")
for title in titles:
    title = title.strip()
    # print urllib2.quote(title)
    link = "<a href=\"https://s3-us-west-1.amazonaws.com/pbc-sermons/" + \
            title.replace(" ", "+").replace("'", "%27") + "\">"
    print link
    f.write(link + "\n")
