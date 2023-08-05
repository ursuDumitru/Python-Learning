import sys

# 1
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

# 2
# python PythonAdvancedTutorial\app4_args.py tata 3.14 "mama hello" 7
# print(sys.argv) # hole array

# 3
# python app4_args.py test.txt "Hello World!"
# filename = sys.argv[1]
# message = sys.argv[2]

# with open(filename, 'w+') as f:
#     f.write(message)

# 4
import getopt

# f - file_name, m - message
# optional parameters
# : - means we expect an input after the option

# python app4_args.py test.txt "Hello World!"
# []
# ['test.txt', 'Hello World!']

# python app4_args.py -f test.txt -m "Hello Dima!"  
# [('-f', 'test.txt'), ('-m', 'Hello Dima!')]
# []
opts, args = getopt.getopt(sys.argv[1:], "f:m:", ['filename', 'message'])

# print(opts)
# print(args)

# default values in case of missing command line arguments
filename = "test1.txt"
message = "Hello Dumitru!"

for opt, arg in opts:
    if opt == '-f':
        filename = arg
    if opt == '-m':
        message = arg

with open(filename, 'w+') as f:
    f.write(message)