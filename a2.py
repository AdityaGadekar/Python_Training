import argparse

# parse = argparse.ArgumentParser(description='sample app',
#                                 fromfile_prefix_chars='@')
# parse.add_argument('-a', action='store_true', default=False)
# parse.add_argument('-b',action='store',dest='b')
# parse.add_argument('-c',action='store',dest='c', type=int)
# print(parse.parse_args(['@abc.txt']))

parser = argparse.ArgumentParser()
parser.add_argument('--three', nargs=3)
parser.add_argument('--optional', nargs='?')
parser.add_argument('--all', nargs='*', dest='all')
parser.add_argument('--one-or-more',nargs='+')
print(parser.parse_args())
