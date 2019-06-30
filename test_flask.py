import requests

r = requests.get(
    'http://127.0.0.1:5000/employee/takehsi'
)
print(r.text)

r = requests.post(
    'http://127.0.0.1:5000/employee', data={'name': 'takeshi'}
)
print(r.text)

r = requests.put(
    'http://127.0.0.1:5000/employee', data={
        'name': 'takeshi', 'new_name': 'watanabe'}
)
print(r.text)

r = requests.delete(
    'http://127.0.0.1:5000/employee', data={'name': 'takeshi'}
)
print(r.text)
