# 1. Создайте класс Обувь. Необходимо хранить следующую информацию:
# ■ тип обуви;
# ✓ мужская,
# ✓ женская;
# ■ вид обуви (кроссовки, сапоги, сандалии, туфли и.т.д.);
# ■ цвет;
# ■ цена;
# ■ производитель;
# ■ размер.
# Создайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Обувь и код для использования модели,
# контроллера и представления.

class Shoe:
    def __init__(self, shoe_type, shoe_style, color, price, manufacturer, size):
        self.shoe_type = shoe_type
        self.shoe_style = shoe_style
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

class ShoeController:
    def create_shoe(self, shoe_type, shoe_style, color, price, manufacturer, size):
        shoe = Shoe(shoe_type, shoe_style, color, price, manufacturer, size)
        return shoe

class ShoeView:
    def display_shoe(self, shoe):
        print("Тип обуви:", shoe.shoe_type)
        print("Вид обуви:", shoe.shoe_style)
        print("Цвет:", shoe.color)
        print("Цена:", shoe.price)
        print("Производитель:", shoe.manufacturer)
        print("Размер:", shoe.size)

controller = ShoeController()
shoe = controller.create_shoe("мужская", "кроссовки", "черный", 100, "Nike", 42)

view = ShoeView()
view.display_shoe(shoe)

# 2. Создайте класс Рецепт. Необходимо хранить следующую информацию:
# ■ название рецепта;
# ■ автор рецепта;
# ■ тип рецепта (первое, второе блюдо и т.д.);
# ■ текстовое описание рецепта;
# ■ ссылка на видео с рецептом;
# ■ список ингредиентов;
# ■ название кухни (итальянская, французская, украинская и т.д.).
# Создайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Рецепт и код для
# использования модели, контроллера и представления. 

class Recipe:
    def __init__(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        self.name = name
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine

class RecipeController:
    def create_recipe(self, name, author, recipe_type, description, video_link, ingredients, cuisine):
        return Recipe(name, author, recipe_type, description, video_link, ingredients, cuisine)

class RecipeView:
    def print_recipe(self, recipe):
        print(f"Recipe: {recipe.name}")
        print(f"Author: {recipe.author}")
        print(f"Type: {recipe.recipe_type}")
        print(f"Description: {recipe.description}")
        print(f"Video Link: {recipe.video_link}")
        print(f"Ingredients: {recipe.ingredients}")
        print(f"Cuisine: {recipe.cuisine}")


controller = RecipeController()
recipe = controller.create_recipe("Pasta Carbonara", "Ramsay Gordon", "Main course",
"Delicious pasta dish with bacon and eggs", "https://www.youtube.com/watch?v=quqbZQvf8oI",
["spaghetti", "bacon", "eggs", "parmesan cheese"], "Italian")

view = RecipeView()
view.print_recipe(recipe)
