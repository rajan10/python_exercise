import requests
import json
import csv

class CsvDataFetcher:
    def __init__(self,url):
        self.url=url
        
    def fetch_data(self):
        try:
            response=requests.get(url=self.url)
            response_json=response.json()
            return response_json
            # print(response_json)
      #      print(type(response_json))    #<class 'dict'>
        except requests.RequestException as exc:
            print(exc)
            
    def make_to_csv(self, data:dict)->None:
        with open("users_list.txt","w", encoding="utf-8") as file_obj:
            header_list =list(data["users"][0].keys())
            dict_writer=csv.DictWriter(file_obj, fieldnames=header_list)  
            dict_writer.writeheader()
            for user in data["users"]:
                dict_writer.writerow(user)
           
    def total_male_greater_than_twenty(self, data:dict)->int:
        # header_list =list(data["users"][0].keys())
        # with open("users_list.txt", "r", encoding="utf-8") as file_obj:
        #     print data["users"]
        male_count=0
        for user in data["users"]:
            gender=user.get("gender", "").lower()
            age=user.get("age",0)
             
            if gender =="male" and age > 20:
                male_count =male_count+1
            
        return male_count

    def find_unique_city(self,data:dict):
        cities=set()
        for user in data["users"]:
            address=user.get("address",{}) #if the key address is not present, it returns an empty address
            city=address.get("city", "").strip() #if the key  city is not present, it returns empty city
            if city:
                cities.add(city)
        return list(cities)    

handler=CsvDataFetcher(url="https://dummyjson.com/users")
response_json=handler.fetch_data()
csv_data=handler.make_to_csv(response_json)
male_count=handler.total_male_greater_than_twenty(response_json)
unique_city=handler.find_unique_city(response_json)
print(unique_city)

