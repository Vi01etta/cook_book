from pprint import pprint
cook_book = {}
with open('cook_book.txt', 'r') as f:
  file_work = f.readlines()
  f.seek(0)   
  for line in file_work:
              dish_name = f.readline().strip()
              if dish_name != '':
                counter = int(f.readline())
                list_of_ingridient = []
                for i in range(counter):
                    temp_dict = {}
                    ingridient = f.readline().strip()
                    separated_ingr = ingridient.split('|')
                    temp_dict['ingredient_name'] = separated_ingr[0]
                    temp_dict['quantity'] = separated_ingr[1]
                    temp_dict['measure'] = separated_ingr[2]
                    list_of_ingridient.append(temp_dict)
                    cook_book[dish_name] = list_of_ingridient
                f.readline().strip()

pprint(cook_book)


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

pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))

