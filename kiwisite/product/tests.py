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

    def test_date_validation(self):
        #add User
        User.objects.create_user('temporary', 'temporary@example.com', "temporary")
        category = Category.objects.create(name = 'category', slug='slug_category',description="desc")
        category.product_set.create(name= 'Trully', slug = "slugy", description='desc',price= 15.5,
                                    created_at=timezone.now()-datetime.timedelta(hours=12),
                                    modified_at=timezone.now() - datetime.timedelta(hours=5)
                                    )
        #login user
        self.client.login(username='temporary', password ='temporary')
        response = self.client.get(reverse('product:secret'), follow=True)

        #user get into secret page
        self.assertContains(response, "that created in range 24 hours")
        #check if product in range 24 hours from now is added to secret page
        self.assertQuerysetEqual(response.context['product_list'], ['<Product: Trully>'])


