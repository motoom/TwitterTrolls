import glob
import isolateids
import isolatescreennames
import prolific
import retweets
import wordcloud

for fn in glob.glob("data/stream_*.json"):
    print "Processing %s" % fn
    
    inputfn = fn

    outputfn = fn.replace(".json", "-ids.txt")
    isolateids.process(inputfn, outputfn)

    outputfn = fn.replace(".json", "-screennames.txt")
    isolatescreennames.process(inputfn, outputfn)

    outputfn = fn.replace(".json", "-prolific.txt")
    prolific.process(inputfn, outputfn)

    outputfn = fn.replace(".json", "-retweets.txt")
    retweets.process(inputfn, outputfn)

    outputfn = fn.replace(".json", "-wordcloud.txt")
    wordcloud.process(inputfn, outputfn)
