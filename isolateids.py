import json

ids = set()

for line in open("data/BhagNawazBhag_stream.txt"):
    ob = json.loads(line)
    id = ob.get("id", 0)
    if id:
        ids.add(id)

with open("data/BhagNawazBhag-ids.txt", "wt") as f:
    f.write("\n".join(str(id) for id in ids))