from tkinter import ttk
from tkinter import *
import json

class Orders:
    def __init__(self, CustomerID, ShipName, ShipAddress, ShipCity, ShipRegion):
        self.CustomerID = CustomerID
        self.ShipName = ShipName
        self.ShipAddress = ShipAddress
        self.ShipCity = ShipCity
        self.ShipRegion = ShipRegion
        self.t = (self.CustomerID, self.ShipName, self.ShipAddress, self.ShipCity, self.ShipRegion)        
    def to_json(self):
        return {"CustomerID": self.CustomerID,"ShipName": self.ShipName,
                     "ShipAddress": self.ShipAddress,"ShipCity": self.ShipCity,"ShipRegion": self.ShipRegion}
    def __str__(self):
       return f"{self.CustomerID} | {self.ShipName} | {self.ShipAddress} | {self.ShipCity} | {self.ShipRegion}"

root = Tk() # создание главного окно 
root.title("Каталог товаров")
#размер окна
root.geometry("1300x500")
root.resizable(True, True)

#Читаем из файла и сохраняем в  список экземпляров класса
orders_list = [] 
with open('output.txt', 'r') as file:
      data = json.load(file)

for i in range(len(data)):
    orders_list.append(Orders(data[i]['CustomerID'], data[i]['ShipName'], data[i]['ShipAddress'], data[i]['ShipCity'], data[i]['ShipRegion'])) # создаем экземляр и добавляем в список

# определяем столбцы таблицы
columns = ("CustomerID", "ShipName", "ShipAddress", "ShipCity", "ShipRegion")
tree = ttk.Treeview(columns = columns, show = "headings")
tree.place(x = 10, y = 10, width = 800, height = 150) 

# определяем заголовки
tree.heading("CustomerID", text = "CustomerID")
tree.heading("ShipName", text = "ShipName")
tree.heading("ShipAddress", text = "ShipAddress")
tree.heading("ShipCity", text = "ShipCity")
tree.heading("ShipRegion", text = "ShipRegion")

#создаем список кортежей
mylist = [obj.t for obj in orders_list]
#print(mylist)

# добавляем данные
for product in mylist:
    tree.insert("", END, values=product)
 
# определяем столбцы
tree1 = ttk.Treeview(columns=columns, show="headings")
tree1.place(x = 10, y = 200, width = 800, height = 150) 
 
# определяем заголовки
tree1.heading("CustomerID", text = "CustomerID")
tree1.heading("ShipName", text = "ShipName")
tree1.heading("ShipAddress", text = "ShipAddress")
tree1.heading("ShipCity", text = "ShipCity")
tree1.heading("ShipRegion", text = "ShipRegion")

#создаем список
languages = ["Sort ShipName", "Sort ShipCity", "ShipRegion == Eastern Europe"]
languages_var = Variable(value=languages)
##listvariable: список элементов, которые добавляются в ListBox
##selectmode: определяет, сколько элементов могут быть выделены
languages_listbox = Listbox(listvariable=languages_var, selectmode=SINGLE)
languages_listbox.place(x=850, y=180) 

#обработка листа
def selected(event):
##curselection(): возвращает набор индексов выделенных элементов
    selected_index = languages_listbox.curselection()
    selected_index = selected_index[0]
# Определяем, какие данные отображать
##delete(first, last = None): удаляет элементы с индексами из диапазона [first, last]. 
    tree1.delete(*tree1.get_children())
    if selected_index == 0:
        l = sorted(mylist, key = lambda x : x[1])
        for product in l:
            tree1.insert("", END, values=product)
    elif selected_index == 1:
        l = sorted(mylist, key = lambda x : x[2])
        for product in l:
            tree1.insert("", END, values=product)
    elif selected_index == 2:
        for product in filter(lambda el: el[-1] == "Eastern Europe", mylist):
            tree1.insert("", END, values=product)
languages_listbox.bind("<<ListboxSelect>>", selected)


def first_button_action():
    btn_1["text"] = f"{len(mylist)}"   

def seconde_button_action():
    btn_2["text"] = f"{len(tree1.get_children())}"

btn_1 = ttk.Button(text="Общее количество записей", command = first_button_action)
btn_1.place(x = 850, y = 100)

btn_2 = ttk.Button(text="Количество отфилтрованных записей", command = seconde_button_action)
btn_2.place(x = 850, y = 150)


root.mainloop()
