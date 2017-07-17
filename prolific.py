import json
import collections
import codecs

def process(inputfn, outputfn):
    twitterers = collections.defaultdict(int)

    with open("data/BhagNawazBhag_stream.txt") as f:
        for line in f:
            ob = json.loads(line)
            # text = ob.get("text", "")
            user = ob.get("user")
            if user:
                username = user.get("name", "")
            if username:
                twitterers[username] += 1

    report = ["Most prolific twitterers (or tweeters? Twitter users?)"]
    for k, v in sorted(twitterers.iteritems(), key=lambda item: item[1], reverse=True):
        msg = u"%s - %d tweets" % (k, v)
        report.append(msg)
        if v < 6:
            break # We're not interested in people with less than 6 tweets

    with codecs.open(outputfn, "w", "utf8") as f:
        f.write("\n".join(report))


if __name__ == "__main__":
    process("data/stream_IndiaIsraelFriendship.json", "data/stream_IndiaIsraelFriendship-prolific.txt")
  
  
  