class Controller:
    def __init__(self, model):
        self.model = model

    def change_composition(self, new_composition):
        self.model.change_composition(new_composition)

    def change_price(self, new_price):
        self.model.change_price(new_price)

    def change_weigth(self, new_weigth):
        self.model.change_weigth(new_weigth)

    def get_all_data(self):
        all_data = self.model.pizza_data
        return all_data

