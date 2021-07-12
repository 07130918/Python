import io

f = io.StringIO()
f.write('test')
f.seek(0)
print(f.read())

f = io.BytesIO()
f.write(b'test')
f.seek(0)
print(f.read())
