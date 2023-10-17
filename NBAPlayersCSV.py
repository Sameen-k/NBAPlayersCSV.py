import requests
import csv

#pip install requests on terminal
#Link for Rapid API
url = "https://free-nba.p.rapidapi.com/players"
#below are the query parameters. (How many results the user want to see at a time)
querystring = {"page":"0","per_page":"25"}

headers = {
	"X-RapidAPI-Key": "4c52c5bc6cmsh6692fee9d27ea15p1c16dcjsnf8cd46958fed",
	"X-RapidAPI-Host": "free-nba.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
page_count = response.json()["meta"]["total_pages"]

#above was from Rapid API
#below is to create the CSV File. parameters have (I) because it's all the pages
with open ("nba.csv", "w") as file:
    writer = csv.writer(file)
    #
    for i in range(page_count):
        querystring = {"page": str(i), "per_page": "100"}
        response = requests.get(url,headers=headers, params=querystring)
        print (i)
        for row in response.json()["data"]:
            writer.writerow([row["id"],row["first_name"] +" "+ row["last_name"], row["position"], row["team"]["full_name"]])

#the +" "+ concatenating adding the first name then the space and then the last name, the space is a delimiter 
    
