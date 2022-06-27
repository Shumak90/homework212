from units import Store, Shop, Request


def main():
    while True:
        user_input = input("Введите запрос: ")
        # user_input = "Доставить 25 сок из склад в магазин"

        if user_input == "стоп":
            break
        request = Request(user_input)

        # print(store.items)
        # print(store.get_free_space)

        from_ = store if request.from_ == 'склад' else shop
        to = store if request.to == 'склад' else shop

        if request.product in from_.items:
            print(f'Нужный товар есть в пункте {request.from_}')
        else:
            print(f'В пункте {request.from_} нет такого товара')
            continue

        if from_.items[request.product] >= request.amount:
            print(f'Нужныое количество есть в пункте {request.from_}')
        else:
            print(f'В пункте {request.from_} не хватает {request.amount - from_.items[request.product]}')
            continue

        if to.get_free_space >= request.amount:
            print(f'В пункте {request.to} достаточно места')
        else:
            print(f'В пункте {request.to} не хватает {request.amount - to.get_free_space}')
            continue

        if request.to == 'магазин' and to.get_unique_items_count == 5 and request.product not in to.items:
            print('В магазине достаточно уникальных значений')
            continue

        from_.remove(request.product, request.amount)
        print(f'Курьер забрал {request.amount} {request.product} из пункта {request.from_}')
        print(f'Курьер везет {request.amount} {request.product} из пункта {request.from_} в пункт {request.to}')
        to.add(request.product, request.amount)
        print(f'Курьер доставил {request.amount} {request.product} в пункт {request.to}')
        print("="*30)
        print('На складе:')
        # print(store.items.items())
        for title, count in store.items.items():
            print(f'{title}: {count}')
        print(f"Свободного места {store.get_free_space}")
        print("=" * 30)
        print('В магазине:')
        # print(shop.items.items())
        for title, count in shop.items.items():
            print(f'{title}: {count}')
        print(f"Свободного места {shop.get_free_space}")
        print("=" * 30)
        # break


if __name__ =="__main__":
    store = Store()
    shop = Shop()

    store_items = {
        "печеньки": 10,
        "молоко": 20,
        "кофе": 12,
        "чай": 15,
        "сок": 25
    }
    store.items = store_items
    main()
