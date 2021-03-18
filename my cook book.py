#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pprint import pprint
cook_book = {}
with open('cook_book.txt', 'r', encoding = 'utf-8') as f:
    while True:
        cook_list = []
        f.seek(0)
        name_of_dish = f.readline().strip()
        count = int(f.readline())
        cook_book[name_of_dish] = cook_list
        for _ in range(count):
            ingr = f.readline().strip()
            splited = ingr.split('|')
            ingridients = {}
            ingridients['ingredient_name'] = splited[0]
            ingridients['quantity'] = splited[1]
            ingridients['measure'] = splited[2]
            cook_list.append(ingridients)
        f.readline()
        if not name_of_dish:
            break
      

pprint(my_book)
            
def get_shop_list_by_dishes(dishes, person_count):
    ingr_dict = {}
    for dish in dishes: 
        for ingr in cook_book[dish]:
            ingr_dict1 = {}
            a = ingr['ingredient_name']
            ingr_dict1['measure'] = ingr['measure'] 
            ingr_dict1['quantity'] = int(ingr['quantity']) * int(person_count)
            if a in ingr_dict:
               ingr_dict1['quantity'] += ingr_dict[a]['quantity']
            ingr_dict[a] = ingr_dict1
    return ingr_dict   


pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))


# In[ ]:





# In[ ]:




