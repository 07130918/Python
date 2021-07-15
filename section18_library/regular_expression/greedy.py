import re

s = '<html><head><title>title</title></head></html>'
print(re.match('<.*>', s))
print(re.match('<.*?>', s))
