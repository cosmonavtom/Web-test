class View:
    def __init__(self, controller):
        self.controller = controller

    def print_all_data(self):
        data = self.controller.get_all_data()
        print(f'Название : {data['name']}\n'
              f'Состав : {', '.join(data['composition'])}\n'
              f'Цена : {data['price']}\n'
              f'Вес : {data['p_weigth']}\n'
              )

    def print_composition_and_weigth(self):
        data = self.controller.get_all_data()
        print(f'Состав : {', '.join(data['composition'])}\n'
              f'Вес : {data['p_weigth']}\n'
              )

    def print_price(self):
        data = self.controller.get_all_data()
        print(f'Цена : {data['price']}\n')

    def change_composition(self, new_composition):
        data = self.controller.get_all_data()
        self.controller.change_composition(new_composition)
        print(f'Состав {data['name']} изменён на {new_composition}')

    def change_price(self, new_price):
        data = self.controller.get_all_data()
        print(f'Цена {data['name']} изменена с {data['price']} на {new_price}')
        self.controller.change_price(new_price)

    def change_weigth(self, new_weigth):
        data = self.controller.get_all_data()
        print(f'Вес {data['name']} изменен с {data['p_weigth']} на {new_weigth}')
        self.controller.change_price(new_weigth)



