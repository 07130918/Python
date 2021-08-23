import requests

payload = {'key1': 'val1', 'key2': 'val2'}


def print_status(r):
    print(r.status_code)
    print(type(r.text))
    print(r.text)
    print(type(r.json()))
    print(r.json())
    print('-' * 60)


# get
r = requests.get('http://httpbin.org/get', params=payload)
print('GET')
print_status(r)

# post
r = requests.post('http://httpbin.org/post', data=payload)
print('POST')
print_status(r)

# put
r = requests.put('http://httpbin.org/put', data=payload)
print('PUT')
print_status(r)

# delete
r = requests.delete('http://httpbin.org/delete', data=payload)
print('DELETE')
print_status(r)
