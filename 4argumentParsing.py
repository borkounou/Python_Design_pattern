
import sys

import getopt



# usage: 4argumentParsing.py FILENAME

filename = sys.argv[1]
message = sys.argv[2]

with open(filename, "w+") as f:
    f.write(message)


opts, args = getopt.getopt(sys.argv[1:], "f:m:",["filename", "message"])
print(opts)
print(args)
