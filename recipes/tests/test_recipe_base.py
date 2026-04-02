from django.test import TestCase
from recipes.models import Category, Recipe, User

class RecipeTestBase(TestCase):
    def setUp(self):
            category = Category.objects.create(name= "category")
            user = User.objects.create_user(
                first_name = 'first',
                last_name = 'name',
                username = 'user',
                password = '123456',
                email = '123@gmail.com',
            )
            recipe = Recipe.objects.create(
                category= category,
                author= user,
                tittle= 'Recipe Tittle',
                description= 'RecipeRecipeRecipeRecipeRecipeRecipe',
                slug= 'Recipe=slug',
                preparation_time= 10,
                preparation_time_unit= 'Minutos',
                sevings= 4,
                sevings_unit= 'Pessoas',
                preparation_steps= 'reciperecipereciperecipereciperecipereciperecipereciperecipe',
                preparation_steps_is_html= False,
                is_published= True ,
            )
            return super().setUp()