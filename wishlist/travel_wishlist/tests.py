from django.test import TestCase
from django.urls import reverse

from .models import Place

class TestViewHomePageIsEmptyList(TestCase):

    def test_load_home_page_shows_empty_list(self):
        response = self.client.get(reverse('places_list'))
        self.assertTemplateUsed(response, 'travel_wishlist/wishlist.html')
        self.assertFalse(response.context['places'])
class TestWishList(TestCase):

    fixtures = ['test_places']
    
    def test_view_wishlist(self):
        response = self.client.get(reverse('place_list'))
        
        self.assertTemplateUsed(response, 'travel_wihslist/wishlist.html')
        
        data_rendered = list(Place.objects.filter(visited=False))
        
        self.assertCountEqual(data_rendered, data_expected)