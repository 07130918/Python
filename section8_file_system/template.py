import string

s = """\
Hi $name
$contents
Have a good day
"""

temp = string.Template(s)
content = temp.substitute(name='Mike', contents='How are you??')
print(content)
