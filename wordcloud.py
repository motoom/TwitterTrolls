import json
import collections
import codecs

def process(inputfn, outputfn):

    wordcloud = collections.defaultdict(int)

    with open("data/BhagNawazBhag_stream.txt") as f:
        for line in f:
            ob = json.loads(line)
            words = ob.get("text", "").lower().split(" ")
            for word in words:
                word = word.strip()
                if not word:
                    continue
                if word.startswith(("#", "@")): # Ignore hashtags and mentions.
                    continue
                wordcloud[word] += 1


    # Remove stopwords from the wordcloud. See http://www.ranks.nl/stopwords
    stopwords = [line.strip().lower() for line in open("data/stopwords.txt").readlines() if line]
    for stopword in stopwords:
        if stopword in wordcloud:
            del wordcloud[stopword]

    top = 30
    report = ["TOP-%d most popular words\n" % top]

    for k, v in sorted(wordcloud.iteritems(), key=lambda item: item[1], reverse=True):
        msg = u"%-6dx %s" % (v, k)
        report.append(msg)
        if top:
            top -= 1
        else:
            break

    with codecs.open(outputfn, "w", "utf8") as f:
        f.write("\n".join(report))


if __name__ == "__main__":
    process("data/stream_IndiaIsraelFriendship.json", "data/stream_IndiaIsraelFriendship-wordcloud.txt")
  
  