import json

def process(inputfn, outputfn):
    nr = 0
    for line in open(inputfn):
        ob = json.loads(line)
        text = ob.get("text", "")
        user = ob.get("user")
        if user:
            username = user.get("name", "")
        print username.encode("utf8")
        print text.encode("utf8")
        print

        if nr > 10:
            break
        else:
            nr += 1

if __name__ == "__main__":
    process("data/stream_IndiaIsraelFriendship.json", None)
    