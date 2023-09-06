import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {'title': 'foo',
        'body': 'bar',
        'userId': 1, }

get_response = requests.post(url=url, data=data)
dict_response = get_response.json()
id = data["userId"]
# id = dict_response.get('userId')
print(id)
