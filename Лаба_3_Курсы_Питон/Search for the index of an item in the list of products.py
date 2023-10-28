# TODO Напишите функцию для поиска индекса товара
def index_product(list, item): #list - список со всеми предметами, item -предмет на проверку
    for i in range(len(list)):
        if item == list[i]: #сравнение предметов из списка и конкретного
            return i #если совпадают выписываем индекс
        else:
            continue #если не совпадают, продолжаем программу
    return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_product(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
