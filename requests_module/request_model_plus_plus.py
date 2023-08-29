import requests
import json
import csv

class CsvDataFetcher:
    def __init__(self,url):
        self.url=url
        
    def fetch_data(self):
        try:
            response=requests.get(self.url)
            
            #print(type(response))  #<class 'requests.models.Response'>
            
            #response_text=response.text
            #print(type(response_text))   #<class 'str'>
           
            response_json=json.loads(response)
            #print(type(response_json))    #<class 'dict'>
            
            #once in dict type, different operations can be performed
            #print(len(response_json["users"]))
                                    
            # users_list= response_json["users"]
            # for user in users_list:
            #     print(user["id"], user["firstName"], user["lastName"])  
            with open("users_list.txt","w") as file_obj:
                headers=make_header()
                dict_reader=csv.DictWriter(file_obj, headers)  
        except requests.RequestException as exc:
            print(exc)
            
    def make_header(data:dict):   
        
        
     
        

handler=CsvDataFetcher(url="https://dummyjson.com/users")
response_json=handler.fetch_data()
handler.make_header(response_json)
