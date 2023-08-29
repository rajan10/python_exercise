import requests
import csv
#using this API, get the data 
#convert to CSV 
class CsvDataFetcher:
    def __init__(self, url):
        self.url=url
    
    def fetch_and_convert_to_csv(self):
        try:
            #make HTTP request 
            r=requests.get(url=url)
            if r.status_code==200:
                lines=r.text.splitlines()  #parse the retrieved object 'r' with .text => to string => and split into multiple lines
                if lines:
                    csv_reader=csv.reader(lines) # using csv module convert the string multiple lines into csv_reader object(iterable)
                else:
                    print("CSV file is empty")
            else:
             print("Error in Http Request/communication")   
        except requests.RequestException as exc:
            print(exc)

def main():
    url="https://dummyjson.com/users"
    data_fetcher=CsvDataFetcher(url)


if __name__=="__main__":
    main()
    


        