from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
# Create your tests here.



class RecipeViewTest(RecipeTestBase):
    
    

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func,  views.home)

    def test_recipe_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_template_shows_no_recie_found_if_no_recipe(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertIn(
            '<h1>Nenhuma receita encontrada</h1>',
            response.content.decode('utf-8')
        )

    def test_recipe_category_view_function_is_correct(self):
        
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func,  views.category)

    def test_recipe_category_view_returns_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:category', kwargs= {'category_id': 1000}))
        self.assertEqual(response.status_code, 404)


    def test_recipe_category_template_loads_recipes(self):
        nedded_tittle= "this is a category test recipe"
        self.make_recipe(tittle= nedded_tittle)
        response = self.client.get(reverse('recipes:category', args=(1,)))
        content = response.content.decode('utf-8')
        
        self.assertIn(nedded_tittle, content)


    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        response_recipes = response.context['recipes']


        content = response.content.decode('utf-8')
        self.assertIn('Recipe Tittle', content)
        self.assertIn('10 Minutos', content)
        self.assertIn('4 Pessoas', content)
        self.assertEqual(len(response_recipes),1)
    

    def test_recipe_detail_template_loads_correct_recipes(self):
            nedded_tittle= "this is a detail page - it loads one recipe"
            self.make_recipe(tittle= nedded_tittle)
            response = self.client.get(reverse('recipes:recipe', kwargs= {'id': 1}))
            content = response.content.decode('utf-8')
            
            self.assertIn(nedded_tittle, content)
            
    def test_recipe_home_template_loads_no_recipes_if_isPublished_false(self):
            """test if don't load the recipies with the isPublished false"""
            self.make_recipe(is_published= False)
            response = self.client.get(reverse('recipes:home'))
            content = response.content.decode('utf-8')
            self.assertIn(
            '<h1>Nenhuma receita encontrada</h1>',
            content
        )
            
    def test_recipe_category_template_loads_no_recipes_if_isPublished_false(self):
            """test if don't load the recipies with the isPublished false"""
            recipe = self.make_recipe(is_published= False)
            response = self.client.get(reverse('recipes:category', kwargs= {'category_id': recipe.category.id}))
            self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_no_recipes_if_isPublished_false(self):
            """test if don't load the recipies with the isPublished false"""
            recipe = self.make_recipe(is_published= False)
            response = self.client.get(reverse('recipes:recipe', kwargs= {'id': recipe.id}))
            self.assertEqual(response.status_code, 404)
        
            
            

            
    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func,  views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:recipe', kwargs= {'id': 1000}))
        self.assertEqual(response.status_code, 404)



    def test_recipe_search_uses_correct_view_function(self):
        view = resolve(reverse("recipes:search"))
        self.assertIs(view.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        url = reverse("recipes:search") + '?q=oi'
        response = self.client.get(url)
        self.assertTemplateUsed(response, "recipes/pages/search.html")

    def test_recipe_search_raises_404_if_no_search_tearm(self):
        response = self.client.get(reverse("recipes:search") )
        self.assertEqual(response.status_code,404) 

        
