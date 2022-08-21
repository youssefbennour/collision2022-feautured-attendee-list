import json
import requests
import csv

url = "https://api.cilabs.com/conferences/cc22/lists/featured_attendees?per_page=40&page="

with open("collision-attendees.csv", "w") as myfile:
    wr = csv.writer(myfile)
    wr. writerow(["first name", "last name", "job title", "country", "image url", "bio"])
    for i in range(1,14):
        r = requests.get(url+str(i))
        data = json.loads(r.text)

        for items in data['data']:
            first_name = items['first_name']
            last_name = items['last_name']
            job_title = items['job_title']
            country = items['country']
            image_url = items['avatar_urls']['original']
            bio = items['bio']
            wr.writerow([first_name, last_name, job_title, country, image_url, bio])
