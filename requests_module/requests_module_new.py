import requests
import csv

class DataFetcher:
    def __init__(self, url):
        self.url = url
      
                        
    def fetch_data(self):
        try:
            response = requests.get(url=self.url)
            response.raise_for_status()
            response_json = response.json()
            return response_json
        except requests.RequestException as exc:
            print(exc)
   
class  CsvWriter:
    def __init__(self,fetched_data: dict, file_location:str):
        self.fetched_data=fetched_data  
        self.file_location=file_location     
            
    def make_to_csv(self)->None:
        with open(self.file_location,"w", encoding="utf-8") as file_obj:
            self.header_list = list(self.fetched_data["users"][0].keys())
            dict_writer = csv.DictWriter(file_obj, fieldnames=self.header_list, lineterminator="\n")  
            dict_writer.writeheader()
            dict_writer.writerows(self.fetched_data["users"])
                   
def total_male_greater_than_twenty(data:dict)->int:    
    male_count=0
    for user in data["users"]:
        gender=user.get("gender", "").lower()
        age=user.get("age",0)
            
        if gender =="male" and age > 20:
            male_count =male_count+1       
    return male_count

def find_unique_city(data:dict)->list[str]:
        cities=set()
        for user in data["users"]:
            address = user.get("address",{}) 
            city = address.get("city", "").strip()
            if city:
                cities.add(city)
        return list(cities)    

handler=DataFetcher(url="https://dummyjson.com/users")
response_json=handler.fetch_data()
csv_writer=CsvWriter(fetched_data=response_json,file_location=r"C:\\Users\\RG\\Desktop\\projects\\python_exercise\\requests_module\\users_list2.csv")

csv_writer.make_to_csv()

male_count=total_male_greater_than_twenty(response_json)
print(f"Total Male Count is: {male_count}")

unique_cities=find_unique_city(response_json)
print(f"The list of unique_cities are: {unique_cities}")


