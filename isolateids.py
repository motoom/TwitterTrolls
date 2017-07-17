import json

def process(inputfn, outputfn):
    ids = set()

    for line in open(inputfn):
        ob = json.loads(line)
        id = ob.get("id", 0)
        if id:
            ids.add(id)

    with open(outputfn, "wt") as f:
        f.write("\n".join(str(id) for id in ids))


if __name__ == "__main__":
    process("data/stream_IndiaIsraelFriendship.json", "data/stream_IndiaIsraelFriendship-ids.txt")
  