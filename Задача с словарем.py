my_dict = {"Яблоки" : 1.5,"Слива" : 1.0,"Картофель":0.5} # словарь.ключ со значением
print(my_dict)
print(type(my_dict))
print(my_dict["Слива"]) #вывод на экран значение ключа слива
my_dict["Яблоки"] = 0.20 # замена значение ключа явлоки
print(my_dict)
my_dict.get ("Помидор")
my_dict.update({"Баклажаны": 1.10,"Капуста": 1.25})# внесение в список других ключей со значениями
print(my_dict)
my_dict.items() # выведение всех ключей с их значениями
my_set = {1,2,3,4,1,2,4,5,"Саша",(0,0,0),"Конфета"} # множество
print(my_set)
print(type(my_set))
my_set.add("Room") # добавление в множество элемента
my_set.remove("Конфета")  # удаление элемента из множества
print(my_set)

