import json
import collections
import codecs

def process(inputfn, outputfn):

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

    report = ["Most retweeted twitter users\n"]
    for k, v in sorted(retweeted.iteritems(), key=lambda item: item[1], reverse=True):
        msg = u"%s - %d retweets" % (k, v)
        report.append(msg)
        if v < 100:
            break # We're not interested in people with less than 100 retweets

    with codecs.open(outputfn, "w", "utf8") as f:
        f.write("\n".join(report))
        
if __name__ == "__main__":
    process("data/stream_IndiaIsraelFriendship.json", "data/stream_IndiaIsraelFriendship-retweets.txt")
  
  