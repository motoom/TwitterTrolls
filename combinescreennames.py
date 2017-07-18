
import sys


def main(argc, argv):
    sets = []
    for fn in argv:
        lines = [line.strip() for line in open(fn).readlines() if line]
        sets.append(set(lines))
    common = set.intersection(*sets)
    msg = "\n".join(common)
    print msg.encode("utf8")
    

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print """Usage:  python combinescreennames.py <file-1> <file-2> <file-3> ... <file-n>
        
Reads the named files, and outputs lines which are common in all files.

For example:

    python combinescreennames.py data/stream_IndiaIsraelFriendship-part-screennames.txt data/stream_ModiInIsrael-part-screennames.txt data/stream_SaveBengal-part-screennames.txt >output.txt
        """
    else:
        sys.argv.pop(0)
        main(len(sys.argv), sys.argv)
