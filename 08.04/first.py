from tkinter import ttk
from tkinter import *
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

class Orders:
    def __init__(self, CustomerID, ShipName, ShipAddress, ShipCity, ShipRegion):
        self.CustomerID = CustomerID
        self.ShipName = ShipName
        self.ShipAddress = ShipAddress
        self.ShipCity = ShipCity
        self.ShipRegion = ShipRegion
    def to_tuple(self):
       return (self.CustomerID, self.ShipName, self.ShipAddress, self.ShipCity, self.ShipRegion)
    def __str__(self):
       return f"{self.CustomerID} | {self.ShipName} | {self.ShipAddress} | {self.ShipCity} | {self.ShipRegion}"

#Читаем из базы и сохраняем в  список экземпляров класса
products_list = [] 
con = sqlite3.connect("northwind.db")
cur = con.cursor()
sqlite_select_query = """SELECT CustomerID, ShipName, ShipAddress, ShipCity, ShipRegion from Orders"""
cur.execute(sqlite_select_query)
records = cur.fetchall()
for row in records:
    products_list.append(Orders(row[0],row[1],row[2],row[3], row[4])) # создаем экземляр и добавляем в список
cur.close()

root=Tk() # создание главного окно 
root.geometry("1100x500") # задание размера окна
root.configure(background="#FFA07A")
style = ttk.Style(root)
style.theme_use('clam')
#создаем список
languages = ["Sort ShipName", "Sort ShipCity", "ShipRegion == Western Europe"]
languages_var = Variable(value=languages)
languages_listbox = Listbox(listvariable=languages_var, selectmode=SINGLE)
languages_listbox.place(x=850, y=130) 

style.configure("Treeview",
                background="blue",          # Цвет фона строк
                foreground="black",            # Цвет текста
                rowheight=25,                  # Высота строки 
                fieldbackground="red")     # Цвет фона ячеек

# CustomerID, ShipName, ShipAddress, ShipCity, ShipRegion
#создаем таблицу
columns = ("CustomerID", "ShipName", "ShipAddress", "ShipCity", "ShipRegion")
tree = ttk.Treeview(columns=columns, show="headings")

# определяем заголовки
tree.heading("CustomerID", text="CustomerID")
tree.heading("ShipName", text="ShipName")
tree.heading("ShipAddress", text="ShipAddress")
tree.heading("ShipCity", text="ShipCity")
tree.heading("ShipRegion", text="ShipRegion")

#создаем список кортежей для добавления в таблицу
mylist = [obj.to_tuple() for obj in products_list]

# добавляем данные в таблицу
for product in mylist:
    tree.insert("", "end", values = product)
tree.place(x=10, y=10, width=800, height=150)  

# определяем столбцы таблицы
tree1 = ttk.Treeview(columns=columns, show="headings")
tree1.place(x=10, y=200, width=800, height=150) 

# определяем заголовки
tree1.heading("CustomerID", text="CustomerID")
tree1.heading("ShipName", text="ShipName")
tree1.heading("ShipAddress", text="ShipAddress")
tree1.heading("ShipCity", text="ShipCity")
tree1.heading("ShipRegion", text="ShipRegion")

#обработка листа
def selected(event):
    selected_index = languages_listbox.curselection()
    selected_index = selected_index[0]
    tree1.delete(*tree1.get_children())
    if selected_index == 0:
        l = sorted(products_list, key = lambda x : x.ShipName)
        for product in l:
            tree1.insert("", END, values=product.to_tuple())
    elif selected_index == 1:
        l = sorted(products_list, key = lambda x : x.ShipCity)
        for product in l:
            tree1.insert("", END, values=product.to_tuple())
    elif selected_index == 2:
        for product in filter(lambda el: el.ShipRegion == "Western Europe", products_list):
            tree1.insert("", END, values=product.to_tuple())
languages_listbox.bind("<<ListboxSelect>>", selected)

#Построение графиков
x=[]
y=[]
for t in products_list:
    x.append(t.ShipName)
    y.append(t.ShipRegion)
def graph():
    figure(figsize=(20,20))
    plt.barh (x, y, height = 0.5, color= '#FFA07A')
    plt.yticks(fontsize = 5)
    plt.title ("")
    plt.show ( )

my_button = Button(root,text = "График №1", bg="#4CAF50",fg="white",font=("Arial", 12, "bold"), command=graph)
my_button.place(x=990,y=100,width=95, height=30)
c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
c7=0
c8=0
c9=0
for t in products_list:
    if t.ShipRegion == "British Isles":
        c1+=1
    elif t.ShipRegion == "Scandinavia":
        c2 += 1
    elif t.ShipRegion == "South America":
        c3 += 1
    elif t.ShipRegion == "Southern Europe":
        c4 += 1
    elif t.ShipRegion == "Western Europe":
        c5 += 1
    elif t.ShipRegion == "North America":
        c6 += 1
    elif t.ShipRegion == "Eastern Europe":
        c7 += 1
    elif t.ShipRegion == "Northern Europe":
        c8 += 1
    elif t.ShipRegion == "Central America":
        c9 += 1
x1= [c1, c2, c3, c4, c5, c6, c7, c8, c9]
y1= ['British Isles', 'Scandinavia', 'South America', 'Southern Europe', 'Western Europe', 'North America', 'Eastern Europe', 'Northern Europe', 'Central America']

def graph1():
    figure(figsize=(10,10))
    plt.pie ( x1,labels = y1 )
    plt.title ("")
    plt.show ()

style = ttk.Style(root)

# Настраиваем стиль для  ttk-кнопок
style.configure('TButton',
                background='green',
                foreground='white',
                font=('Arial', 12, 'bold'))
my_button1 = ttk.Button(root,text = "График №2", command=graph1)
my_button1.place(x=990,y=300,width=100, height=30)
root.mainloop()

