class Pizza:

    def __init__(self, name, composition, price, p_weigth):
        self.pizza_data = {
            'name': name,
            'composition': composition,
            'price': price,
            'p_weigth': p_weigth,
        }

    def change_composition(self, new_composition):
        self.pizza_data['composition'].clear()
        for composition in new_composition:
            self.pizza_data['composition'].append(composition)


    def change_price(self, new_price):
        self.pizza_data['price'] = new_price

    def change_weigth(self, new_weigth):
        self.pizza_data['p_weigth'] = new_weigth

    def get_all_data(self):
        return self.pizza_data

