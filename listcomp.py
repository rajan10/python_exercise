# import requests
# urls= ('http://headfirstlabs.com', 'http://oreally.com', 'http://twitter.com')
# for resp in (requests.get(url) for url in urls):
#     print(len(resp.content), '->', resp.status_code, '->' , resp.url)

def simple_generator():
    yield 1
    yield 2
    print("hello ")
    print("world")


generator_object = simple_generator()
for i in generator_object:
    # Do function call or processing with yield element
    print(i)
