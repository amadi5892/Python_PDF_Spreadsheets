# ---- Task 1 ----
import csv

data = open('link.csv',encoding='utf-8')
csv_data = csv.reader(data,delimiter=',',quotechar='"')
data_lines = list(csv_data)
print(len(data_lines))


count = 0
x = 1
y = 0 
chars = []
while count < 66:
    entry = data_lines[x][y]
    chars.append(entry)
    count += 1
    x += 1
    y += 1

print(chars)
link = ''.join(chars)
print(link)