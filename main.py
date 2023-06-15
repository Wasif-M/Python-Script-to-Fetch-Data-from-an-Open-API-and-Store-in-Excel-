import requests,json
from openpyxl import Workbook

url="https://parallelum.com.br/fipe/api/v1/carros/marcas"
response=requests.get(url)

if response.status_code==200:
    data=json.loads(response.text)
    print(data)
else:
    print("Error, while fetching data from the API")
    exit(1)

workbook = Workbook()
worksheet = workbook.active
for item in data:
    values = list(item.values())
    worksheet.append(values)

file_path = "data.xlsx"  
workbook.save(file_path)
try:
    workbook.save(file_path)
    print("Data saved to excel file successfully")

except Exception as e:
    print("An error occurred:", str(e))









