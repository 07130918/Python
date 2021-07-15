import re

m = re.match('ab?', 'abb')
print(m)

print('-' * 60)
m = re.match('ab*', 'abbbcccc')
print(m)

print('-' * 60)
m = re.match('ab+', 'abb')
print(m)

print('-' * 60)
m = re.match('a{2,4}', 'aaaaaab')
print(m)

print('-' * 60)
m = re.match('\w', '_')
print(m)

print('-' * 60)
m = re.match('\d', '1234')
print(m)

print('-' * 60)
m = re.match('(a|b)+', 'aaaabbbff')
print(m)

print('-' * 60)
m = re.match('\*', '*')
print(m)

print('-' * 60)
m = re.search('^abc', 'abcabcabc')
print(m)

print('-' * 60)
m = re.search('abc$', 'abctest ffabc')
print(m)
