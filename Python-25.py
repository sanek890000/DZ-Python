# 1. Создайте приложение для эмуляции работа киоска по продаже хот-догов. Приложение должно иметь
# следующую функциональность:
# 1. Пользователь может выбрать из трёх стандартных
# рецептов хот-дога или создать свой рецепт.
# 2. Пользователь может выбирать добавлять ли майонез,
# горчицу, кетчуп, топпинги (сладкий лук, халапеньо,
# чили, соленный огурец и т.д.).
# 3. Информацию о заказанном хот-доге нужно отображать на экран
# и сохранять в файл.
# 4. Если пользователь заказывает от трёх хот-догов нужно
# предусмотреть скидку. Скидка зависит от количества
# хот-догов.
# 5. Расчет может производиться, как наличными, так и
# картой.
# 6. Необходимо иметь возможность просмотреть коли-
# чество проданных хот-догов, выручку, прибыль.
# 7. Необходимо иметь возможность просмотреть информацию
# о наличии компонентов для создания хот-дога.
# 8. Если компоненты для создания хот-догов заканчиваются
# нужно вывести информационное сообщение
# о тех компонентах, которые требуется приобрести.
# 9. Классы приложения должны быть построены с уче-
# том принципов SOLID и паттернов проектирования.

# Вариант - 1

import json
import os

class Inventory:
    def __init__(self):
        self.components = {
            "bun": 50,
            "sausage": 100,
            "mayonnaise": 30,
            "mustard": 30,
            "ketchup": 50,
            "sweet_onion": 20,
            "jalapeno": 20,
            "chili": 30,
            "pickle": 30
        }

    def check_availability(self, recipe):
        for item, amount in recipe.items():
            if self.components.get(item, 0) < amount:
                return False, item
        return True, None

    def use_components(self, recipe):
        for item, amount in recipe.items():
            if self.components.get(item, 0) >= amount:
                self.components[item] -= amount
            else:
                raise Exception(f"Недостаточно компонента: {item}")

    def restock_item(self, item, amount):
        self.components[item] = self.components.get(item, 0) + amount

    def display_low_stock_items(self):
        low_stock_items = {item: amount for item, amount in self.components.items() if amount < 5}
        if low_stock_items:
            print("Пополните запасы следующих компонентов:")
            for item, amount in low_stock_items.items():
                print(f"{item}: {amount} осталось")
        else:
            print("Все компоненты в достаточном количестве.")

class HotDog:
    def __init__(self, name, recipe):
        self.name = name
        self.recipe = recipe

    def __str__(self):
        return self.name

class StandardHotDogFactory:
    @staticmethod
    def create_hotdog(option):
        standard_recipes = {
            "1": HotDog("Классический хот-дог", {"bun": 1, "sausage": 1, "mustard": 1}),
            "2": HotDog("Чили-дог", {"bun": 1, "sausage": 1, "chili": 1, "ketchup": 1}),
            "3": HotDog("Пикантный хот-дог", {"bun": 1, "sausage": 1, "jalapeno": 1, "sweet_onion": 1}),
        }
        return standard_recipes.get(option)

class CustomHotDogFactory:
    @staticmethod
    def create_hotdog(custom_name, custom_recipe):
        recipe = {"bun": 1, "sausage": 1}
        recipe.update(custom_recipe)
        return HotDog(custom_name, recipe)

class Order:
    def __init__(self):
        self.hotdogs = []
        self.total_price = 0.0
        self.final_price = 0.0

    def add_hotdog(self, hotdog):
        self.hotdogs.append(hotdog)
        self.total_price += 150  # Базовая цена за хот-дог
        self.update_final_price()

    def update_final_price(self):
        count = len(self.hotdogs)
        if count >= 3:
            self.final_price = self.total_price * 0.9  # 10% скидка
        else:
            self.final_price = self.total_price

    def display_order(self):
        for idx, hotdog in enumerate(self.hotdogs, 1):
            print(f"{idx}. {hotdog}")
        print(f"Общая стоимость: {self.final_price:.2f}")

    def save_order(self):
        order_data = {
            "hotdogs": [str(hotdog) for hotdog in self.hotdogs],
            "final_price": self.final_price
        }
        with open("orders.txt", "a") as f:
            f.write(json.dumps(order_data) + "\\n")

class PaymentStrategy:
    def pay(self, amount):
        raise NotImplementedError

class CashPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата наличными: {amount:.2f} руб.")
        return True

class CardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата картой: {amount:.2f} руб.")
        return True

class MainApp:
    def __init__(self):
        self.inventory = Inventory()
        self.orders = []
        self.revenue = 0.00

    def display_menu(self):
        print("Добро пожаловать в хот-дог киоск!")
        print("1. Классический хот-дог")
        print("2. Чили-дог")
        print("3. Пикантный хот-дог")
        print("4. Создать собственный хот-дог")
        print("5. Просмотр заказа")
        print("6. Оплата заказа")
        print("7. Просмотр выручки")
        print("8. Просмотр компонентов")
        print("9. Выйти")

    def create_order(self):
        order = Order()
        while True:
            self.display_menu()
            choice = input("Выберите опцию: ")
            if choice in ["1", "2", "3"]:
                hotdog = StandardHotDogFactory.create_hotdog(choice)
                available, missing_item = self.inventory.check_availability(hotdog.recipe)
                if available:
                    self.inventory.use_components(hotdog.recipe)
                    order.add_hotdog(hotdog)
                else:
                    print(f"Недостаточно компонента: {missing_item}")
            elif choice == "4":
                custom_name = input("Введите название своего хот-дога: ")
                custom_recipe = {}
                while True:
                    component = input("Введите компонент (или 'готово' для завершения): ")
                    if component == "готово":
                        break
                    amount = int(input(f"Введите количество {component}: "))
                    custom_recipe[component] = amount
                hotdog = CustomHotDogFactory.create_hotdog(custom_name, custom_recipe)
                available, missing_item = self.inventory.check_availability(hotdog.recipe)
                if available:
                    self.inventory.use_components(hotdog.recipe)
                    order.add_hotdog(hotdog)
                else:
                    print(f"Недостаточно компонента: {missing_item}")
            elif choice == "5":
                order.display_order()
            elif choice == "6":
                payment_choice = input("Оплата наличными или картой? (наличные/карта): ")
                if payment_choice == "наличные":
                    payment_strategy = CashPayment()
                else:
                    payment_strategy = CardPayment()
                if payment_strategy.pay(order.final_price):
                    order.save_order()
                    self.orders.append(order)
                    self.revenue += order.final_price
                    print("Заказ успешно оплачен!")
                break
            elif choice == "7":
                print(f"Общая выручка: {self.revenue:.2f} руб.")
            elif choice == "8":
                self.inventory.display_low_stock_items()
            elif choice == "9":
                break
            else:
                print("Некорректный выбор, попробуйте снова.")

if __name__ == "__main__":
    app = MainApp()
    while True:
        app.create_order()





# Вариант - 2

import json

class Ingredient:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

class HotDog:
    def __init__(self, name, ingredients, base_price):
        self.name = name
        self.ingredients = ingredients
        self.base_price = base_price

class Inventory:
    def __init__(self):
        self.ingredients = {
            "Булочка": Ingredient("Булочка", 50),
            "Сосиска": Ingredient("Сосиска", 50),
            "Майонез": Ingredient("Майонез", 50),
            "Горчица": Ingredient("Горчица", 50),
            "Кетчуп": Ingredient("Кетчуп", 50),
            "Сладкий лук": Ingredient("Сладкий лук", 20),
            "Халапеньо": Ingredient("Халапеньо", 20),
            "Чили": Ingredient("Чили", 20),
            "Соленый огурец": Ingredient("Соленый огурец", 20),
        }

    def check_availability(self, required_ingredients):
        for ing, qty in required_ingredients.items():
            if self.ingredients[ing].quantity < qty:
                return False
        return True

    def deduct_ingredients(self, used_ingredients):
        for ing, qty in used_ingredients.items():
            self.ingredients[ing].quantity -= qty

    def restock(self, ing_name, qty):
        if ing_name in self.ingredients:
            self.ingredients[ing_name].quantity += qty

    def get_low_stock(self):
        low_stock_items = {}
        for ing_name, ing in self.ingredients.items():
            if ing.quantity < 10:
                low_stock_items[ing_name] = ing.quantity
        return low_stock_items

class Kiosk:
    def __init__(self):
        self.inventory = Inventory()
        self.sales_data = []
        self.hotdogs = {
            "Классический": HotDog("Классический", {"Булочка": 1, "Сосиска": 1, "Кетчуп": 1, "Горчица": 1}, 100),
            "Американский": HotDog("Американский", {"Булочка": 1, "Сосиска": 1, "Майонез": 1, "Сладкий лук": 1}, 120),
            "Мексиканский": HotDog("Мексиканский", {"Булочка": 1, "Сосиска": 1, "Чили": 1, "Халапеньо": 1}, 150)

        }

    def show_menu(self):
        print("Меню хот-догов:")
        for hotdog_name, hotdog in self.hotdogs.items():
            print(f"{hotdog_name} - {hotdog.base_price} руб.")

    def create_hotdog(self):
        print("Создание хот-дога:")
        custom_ingredients = {}
        custom_ingredients["Булочка"] = 1
        custom_ingredients["Сосиска"] = 1
        optional_ingredients = ["Майонез", "Горчица", "Кетчуп", "Сладкий лук", "Халапеньо", "Чили", "Соленый огурец"]

        for opt_ing in optional_ingredients:
            add_ing = input(f"Добавить {opt_ing}? (да/нет): ").strip().lower()
            if add_ing == "да":
                if opt_ing in custom_ingredients:
                    custom_ingredients[opt_ing] += 1
                else:
                    custom_ingredients[opt_ing] = 1

        # Определение цены на основе ингредиентов
        base_price = 100 + sum([20 for _ in custom_ingredients if custom_ingredients[_]>1])

        return HotDog("Кастомный", custom_ingredients, base_price)

    def place_order(self):
        self.show_menu()
        choice = input("Выберите хот-дог или введите 'кастомный' для создания своего: ").strip().lower()
        if choice in self.hotdogs:
            selected_hotdog = self.hotdogs[choice]
        elif choice == 'кастомный':
            selected_hotdog = self.create_hotdog()
        else:
            print("Некорректный выбор")
            return

        quantity = int(input("Введите количество: ").strip())
        if self.inventory.check_availability(selected_hotdog.ingredients):
            self.inventory.deduct_ingredients(selected_hotdog.ingredients)
            self.sales_data.append({"hotdog": selected_hotdog.name, "quantity": quantity, "price": selected_hotdog.base_price * quantity})

            total_price = selected_hotdog.base_price * quantity
            if quantity >= 3: # Простой расчет скидки
                total_price *= 0.90  # 10% скидка
            payment_method = input("Выберите метод оплаты (наличные/карта): ").strip().lower()
            print(f"Ваш заказ: {selected_hotdog.name}, Количество: {quantity}, Итого: {total_price} руб, Оплата: {payment_method}")
            self.save_order(selected_hotdog.name, quantity, payment_method)
        else:
            print("Недостаточно ингредиентов для приготовления")

    def save_order(self, hotdog_name, quantity, payment_method):
        with open("orders.txt", "a") as file:
            file.write(f"{hotdog_name},{quantity},{payment_method}\\n")

    def show_sales_stats(self):
        total_hotdogs = sum(order['quantity'] for order in self.sales_data)
        total_revenue = sum(order['price'] for order in self.sales_data)
        print(f"Продано хот-догов: {total_hotdogs}")
        print(f"Выручка: {total_revenue} руб")

    def check_inventory(self):
        low_stock = self.inventory.get_low_stock()
        if low_stock:
            print("Низкий уровень ингредиентов:")
            for ing, qty in low_stock.items():
                print(f"{ing}: {qty} осталось")
        else:
            print("Все ингредиенты в достаточном количестве")

if __name__ == "__main__":
    kiosk = Kiosk()

    while True:
        print("1. Показать меню")
        print("2. Сделать заказ")
        print("3. Показать статистику продаж")
        print("4. Проверить наличие ингредиентов")
        print("5. Выход")

        choice = input("Выберите действие: ").strip()
        if choice == "1":
            kiosk.show_menu()
        elif choice == "2":
            kiosk.place_order()
        elif choice == "3":
            kiosk.show_sales_stats()
        elif choice == "4":
            kiosk.check_inventory()
        elif choice == "5":
            break
        else:
            print("Некорректный ввод, попробуйте снова")