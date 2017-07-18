import json
import codecs

def process(inputfn, outputfn):
    report = []
    for line in open(inputfn):
        ob = json.loads(line)
        text = ob.get("text", "").replace("\n", " ").replace("  ", " ").strip()
        user = ob.get("user")
        username = "unknown"
        if user:
            username = user.get("screen_name", "")
        msg = u"%s: %s" % (username, text)
        report.append(msg)

    with codecs.open(outputfn, "w", "utf8") as f:
        f.write("\n".join(report))
        
if __name__ == "__main__":
    process("data/stream_IndiaIsraelFriendship-part.json", "data/stream_IndiaIsraelFriendship-part-tweets.txt")
   