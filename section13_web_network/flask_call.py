import requests

r = requests.post('http://127.0.0.1:5000/post', data={'name': 'kota'})
print(r.text)

r = requests.post('http://127.0.0.1:5000/employee', data={'name': 'kota'})
print(r.text)

r = requests.get('http://127.0.0.1:5000/employee/kota')
print(r.text)

r = requests.put('http://127.0.0.1:5000/employee', data={
    'name': 'kota',
    'new_name': 'rikudou-sennin'
})
print(r.text)

r = requests.delete('http://127.0.0.1:5000/employee', data={
    'name': 'rikudou-sennin'
})
print(r.text)
