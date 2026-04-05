from recipes.tests.test_recipe_base import RecipeTestBase
from django.core.exceptions import ValidationError

from parameterized import parameterized

class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()
    

    def test_the_test(self):
        recipe = self.recipe.tittle = 'A' * 70

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()


    @parameterized.expand([
            ('tittle', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('sevings_unit', 65),
        ])
    def test_recipe_fields_max_length(self,field,max_length):
        setattr(self.recipe, field, "A" * (max_length+1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

 