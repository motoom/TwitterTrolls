import json

nr = 0
for line in open("data/BhagNawazBhag_stream.txt"):
    ob = json.loads(line)
    text = ob.get("text", "")
    user = ob.get("user")
    if user:
        username = user.get("name", "")
    print username
    print text.encode("utf8")
    print

    if nr > 10:
        break
    else:
        nr += 1


#shobzwashere
# I think it worked! greetings from Michiel, motoom@xs4all.nl
