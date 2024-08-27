from Pizza.pizza_creator import PizzaCreator, CreateMenuPizza, CreateOwnPizza
from Pasta.pasta_creator import PastaCreator, CreateMenuPasta, CreateOwnPasta


def pizza_client_code(creator: PizzaCreator, order: str):
    creator.add_additional_ingredient()
    print(creator.make_pizza(order))
    print(creator.bake_pizza(order))
    print(creator.save_order_to_json(order))


def pasta_client_code(creator: PastaCreator, order: str):
    creator.add_additional_ingredient()
    print(creator.make_pasta(order))
    print(creator.cook_pasta(order))
    print(creator.save_order_to_json(order))


if __name__ == "__main__":
    choice = input('Желаете пиццу(1) или пасту(2): ').lower()
    if choice in ('1', 'пицца', 'пиццу', 'pizza'):
        menu = ["Гавайская", "Грибная", "Сырный цыпленок", "Пепперони", "Тунец - тысяча островов"]
        print(f'Наше меню - {menu}')
        user_order = input("Введите ваш заказ: ")
        if user_order in menu:
            pizza_client_code(CreateMenuPizza(), user_order)
        else:
            pizza_client_code(CreateOwnPizza(), user_order)
    elif choice in ('2', 'паста', 'пасту', 'pasts'):
        menu = ["Карбонара", "Болоньезе", "Фетучини"]
        print(f'Наше меню - {menu}')
        user_order = input("Введите ваш заказ: ")
        if user_order in menu:
            pasta_client_code(CreateMenuPasta(), user_order)
        else:
            pasta_client_code(CreateOwnPasta(), user_order)
    else:
        print('Ошибка ввода')

