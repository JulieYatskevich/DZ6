import json
import csv
import openpyxl


username = input()
age = input()
user =f'{username}:{age}'

with open ("users.json", "a") as write_file:
    json.dump(user, write_file)



with open('users.csv', 'w') as write2_file:
    writer = csv.writer(write2_file)
    writer.writerow([user])



book = openpyxl.Workbook()
sheet = book.active
sheet['A1'] = username
sheet['B1'] = age
book.save('Juliebook.xlsx')
book.close()