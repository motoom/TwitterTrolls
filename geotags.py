import json

withcoord = withoutcoord = 0

for line in open("data/stream_GSTForNewIndia.json"):
    ob = json.loads(line)
    coords = ob.get("coordinates", 0)
    if coords:
        print coords
        withcoord += 1
    else:
        withoutcoord += 1
        
print "%d tweets with coordinates, and %d without. %d total." % (withcoord, withoutcoord, withcoord+withoutcoord)
