from django.test import TestCase

from .models import MenuItem


class MenuItemTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
    def test_get_item(self):
        item = MenuItem.objects.get(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)
        self.assertEqual(item.inventory, 100)