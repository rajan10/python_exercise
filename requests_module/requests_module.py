import requests

url="https://dummyjson.com/users"
try:
    #Make a GET request to a websitemyjson.com/users"
    r=requests.get(url=url, timeout= 0.004, verify=True) 
    error_status_code=r.raise_for_status()
    print(error_status_code)
    print("Successful request")
except requests.exceptions.HTTPError as exc:    
    print("HTTP Error")
    print(exc.args[0])  
except requests.exceptions.ReadTimeout as errrt:
    print("Time out ")
    print(errrt.args[0])
except requests.exceptions.ConnectionError as errce:
    print("Connection Error")
    print(errce.args[0])
except requests.exceptions.RequestException as errer:
    print("Request Exception Error")
    print((errer.args[0]))
    
   
    

# try:
#     response=requests.get(url=url)  #returns response object
#     #print(response.status_code())
#     print(response)
    
#     response_text=response.__format__
#     print(response_text)
#     print(type(response_text))
  
    
# except:
#     print("something wrong")
# #requests.models.Response