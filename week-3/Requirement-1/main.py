import json
import urllib.request as request
import csv

src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    #data=response.read().decode("utf-8")
    data = json.load(response) #利用json模組處理json資料

tourAttraction = data['result']['results']

with open('.data.csv','w', newline='') as csvfile:
    
    writer = csv.writer(csvfile)
    writer.writerow(['景點名稱','區域','經度','緯度','第一張圖檔網址'])

    for spot in tourAttraction:
        stitle = spot['stitle']
        addr=spot['address'].split()
        dist = addr[1][0:3]
        
        longitude = spot['longitude']
        latitude = spot['latitude']
        
        spotList = spot['file'].lower().split('.jpg')
        imgUrl = (spotList[0] + ".jpg")

        writer.writerow([stitle,dist,longitude,latitude,imgUrl])