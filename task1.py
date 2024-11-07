
items_list = ['арбуз', 'апельсин', 'банан', 'ананас', 'киви', 'банан']

def find_index(request):
    for i in range(len(items_list)):
        if request is items_list[i]:
            return i

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index('апельсин')  
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
        break
    else:
        print(f"Товар не найден в списке.")
        break
