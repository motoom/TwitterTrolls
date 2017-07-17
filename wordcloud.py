import json
import collections
import pprint

wordcloud = collections.defaultdict(int)

with open("data/BhagNawazBhag_stream.txt") as f:
    for line in f:
        ob = json.loads(line)
        words = ob.get("text", "").lower().split(" ")
        for word in words:
            wordcloud[word] += 1
        

print "Most popular words\n"

top = 30

for k, v in sorted(wordcloud.iteritems(), key=lambda item: item[1], reverse=True):
    msg = u"%-6dx %s" % (v, k)
    print msg.encode("utf8")

    if top:
        top -= 1
    else:
        break
