from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from .models import Product, Category

from django.utils import timezone
import datetime

# Create your tests here.

class SecretPageTest(TestCase):

    def test_non_authenticated_user(self):
        response = self.client.get(reverse('product:secret'))
        self.assertEqual(response.status_code, 302)

    def test_user_login(self):
        user = User.objects.create_user('temporary', 'temporary@example.com', "temporary")
        self.client.login(username='temporary', password ='temporary')
        response = self.client.get(reverse('product:secret'), follow=True)
        self.assertEqual(response.status_code, 200)

    # def test_date_validation(self):
    #     User.objects.create_user('temporary', 'temporary@example.com', "temporary")
    #     category = Category.objects.create('category', 'slug_category', "desc")
    #     set_all = category.product_set.all()
    #     product = Product.objects.create(
    #         name = 'Trully',
    #         price = 15.5,
    #         created_at=timezone.now()-datetime.timedelta(hours=12),
    #         modified_at = timezone.now() - datetime.timedelta(hours=5),
    #         slug = "slugy",
    #         description = 'desc',
    #     )
    #
    #     self.client.login(username='temporary', password ='temporary')
    #     response = self.client.get(reverse('product:secret'), follow=True)
    #
    #     #user get into secret page
    #     self.assertContains(response, "that created in range 24 hours")
    #     #self.assertQuerysetEqual(response.context['product_list'], ['<Product: Trully>'])


