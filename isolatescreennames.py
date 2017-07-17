import json

def process(inputfn, outputfn):
    screennames = set()

    for line in open(inputfn):
        ob = json.loads(line)
        user = ob.get("user")
        if user:
            screenname = user.get("screen_name")
        if screenname:
            screennames.add(screenname)
        
    with open(outputfn, "wt") as f:
        f.write("\n".join(sorted(screennames)))
    
    
if __name__ == "__main__":
    process("data/stream_IndiaIsraelFriendship.json", "data/stream_IndiaIsraelFriendship-screennames.txt")
  