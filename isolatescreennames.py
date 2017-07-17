import json

screennames = set()

for line in open("data/BhagNawazBhag_stream.txt"):
    ob = json.loads(line)
    user = ob.get("user")
    if user:
        screenname = user.get("screen_name")
    if screenname:
        screennames.add(screenname)
        

with open("data/BhagNawazBhag-screennames.txt", "wt") as f:
    f.write("\n".join(sorted(screennames)))