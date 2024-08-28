from Model import Pizza
from Controller import Controller
from View import View

name = 'Пепперони'
composition = ['свинина', 'говядина', 'паприка', 'острый перец']
price = 800
p_weigth = 450

pizza = Pizza(name, composition, price, p_weigth)
controller = Controller(pizza)
view = View(controller)

# TEST
# Показываем всё
view.print_all_data()
# Изменяем состав и вес
view.change_composition(['колбаса', 'перец'])
view.change_weigth(500)
# Смотрим только состав и вес
view.print_composition_and_weigth()
# Изменяем цену
view.change_price(1000)
# Смотрим только цену
view.print_price()
# Снова смотрим всю инфу
view.print_all_data()
