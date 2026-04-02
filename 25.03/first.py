import csv
import json
import sqlite3

class Orders:
    def __init__(self, CustomerID, ShipName, ShipAddress, ShipCity, ShipRegion):
        self.CustomerID = CustomerID
        self.ShipName = ShipName
        self.ShipAddress = ShipAddress
        self.ShipCity = ShipCity
        self.ShipRegion = ShipRegion

##Преобразует объект в словарь для json
    def to_json(self):
        return {"CustomerID": self.CustomerID,"ShipName": self.ShipName,
             "ShipAddress": self.ShipAddress,"ShipCity": self.ShipCity,
             "ShipRegion": self.ShipRegion}

##Преобразует объект в список для CSV
    def to_list(self):
        return [self.CustomerID, self.ShipName, self.ShipAddress, self.ShipCity, self.ShipRegion]
    def __str__(self):
        return f"{self.CustomerID} {self.ShipName} {self.ShipAddress} {self.ShipCity} {self.ShipRegion}"


con = sqlite3.connect("northwind.db")
cur = con.cursor()
sqlite_select_query = """SELECT CustomerID, ShipName, ShipAddress, ShipCity, ShipRegion from Orders"""
cur.execute(sqlite_select_query)
records = cur.fetchall()

products_list  = []
for row in records:
    products_list.append(Orders(row[0],row[1],row[2],row[3], row[4])) # создаем экземляр и добавляем в список
cur.close()

for i in range(len(products_list)):
    print(products_list[i])

# Запись бд в json формат
temp =[]
for i in range(len(products_list)):
        temp.append(products_list[i].to_json())
with open('output.txt', 'w') as file:
    json.dump(temp, file)

# Запись в csv таблицу
with open('pro.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['CustomerID', 'ShipName', 'ShipAddress', 'ShipCity', 'ShipRegion'])
    for p in products_list:
        writer.writerow(p.to_list())

# №1
dict_of_ShipRegion = {}
for order in products_list:
    if order.ShipRegion not in dict_of_ShipRegion:
        dict_of_ShipRegion[order.ShipRegion] = 1
    else:
        dict_of_ShipRegion[order.ShipRegion] += 1
print(dict_of_ShipRegion)

# №2
print(*sorted(dict_of_ShipRegion.items(), key = lambda x: x[1], reverse = True)[:3], sep = '\n')

# №3
print(len(dict_of_ShipRegion.keys()))

# №4
for one in dict_of_ShipRegion.keys():
    if one[0] in 'Nn':
        print(one)