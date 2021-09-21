import argparse
# parse = argparse.ArgumentParser(description="example")
# parse.add_argument('-a', action="store_true", default=False)
# parse.add_argument('-b', action="store", dest='b')
# parse.add_argument('-c', action="store", dest='c', type=int)
# print(parse.parse_args(['-a', '-bonkar', '-c', '3']))

# parse = argparse.ArgumentParser(description="test")
# parse.add_argument('count', action='store', type=int)
# parse.add_argument('units', action='store')
# parse.add_argument('measurement', action='store')
# parse.add_argument('length', action='store', type=int)
# print(parse.parse_args())

# Action
# Store
# store_const
# store_false, store_true
# append []
# append_const

parser = argparse.ArgumentParser()
parser.add_argument('-s', action='store', dest='simple_value', help='store simple value')
parser.add_argument('-c', action='store_const', dest='constant_value',
                    const='value-to-store', help='store constant value')
parser.add_argument('-t', action='store_true', default=False,
                    dest='boolean_switch', help='set a switch to true')
parser.add_argument('-f', action='store_false', default=False,
                    dest='boolean switch', help='set a switch to false')
parser.add_argument('-a', action='append', dest='collection', default=[],
                    help='add repeated value to list')
parser.add_argument('-A', action='append_const', dest='const_collection',
                    const='value-1-to-append', help='Add different value to list')
parser.add_argument('--version', action='version', version='1.0')
result = parser.parse_args()
print('simple_value = ', result.simple_value)
print('const_value = ', result.constant_value)
print('boolean switch =', result.boolean_switch)
print('collection =', result.collection)
print('const_collection=', result.const_collection)
