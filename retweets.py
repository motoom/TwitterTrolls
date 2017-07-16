import json
import collections
import pprint

retweeted = collections.defaultdict(int)

with open("data/BhagNawazBhag_stream.txt") as f:
    for line in f:
        ob = json.loads(line)

        user = ob.get("user")
        if user:
            username = user.get("name", "")

        quoted = ob.get("quoted_status")
        if quoted:
            retweets = quoted.get("retweet_count", 0)
            retweeted[username] += retweets


print "Most retweeted twitter users\n"

for k, v in sorted(retweeted.iteritems(), key=lambda item: item[1], reverse=True):
    msg = u"%s - %d retweets" % (k, v)
    print msg.encode("utf8")
    if v < 100:
        break # We're not interested in people with less than 100 retweets
