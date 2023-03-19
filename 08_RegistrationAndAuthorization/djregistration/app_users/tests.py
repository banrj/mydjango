from django.test import TestCase
from django.urls import reverse
from app_users.models import Profile, Product, Order
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission


class ProductCreateViewTestCase(TestCase):
    def setUp(self) -> None:
        User = get_user_model()
        user = User.objects.create_superuser(username='danil', password='134pass')
        Profile.objects.create(user=user)

    def test_create_product(self):
        User = get_user_model()
        user = User.objects.get(username='danil')
        self.client.login(username='danil', password='134pass')

        response = self.client.post(
            reverse('creat-product'),
            {
                "created_by": user.profile,
                'product_name': "microphone",
                'price': 455,
                'options': "Good sound"

             }
        )
        self.assertRedirects(response, reverse('main'))


class ProductDetailViewTestCase(TestCase):
    def setUp(self) -> None:
        User = get_user_model()
        self.user = User.objects.create_user(username='danil', password='134pass')
        self.user.user_permissions.add(Permission.objects.get(codename='change_product'))
        Profile.objects.create(user=self.user)
        self.client.login(username='danil', password='134pass')
        self.product = Product.objects.create(product_name="microphone", price=12, created_by=self.user.profile)

    def tearDown(self) -> None:
        self.user.delete()
        self.product.delete()

    def test_get_product(self):
        self.client.get(
            'product-detail', kwargs={'pk': self.product.id}
        )


class OrderDetailViewTestCase(TestCase):
    fixtures = [
        "products-fixture.json",
        "profile-fixture.json",
        'users-fixture.json',
    ]

    @classmethod
    def setUpClass(cls):
        super(OrderDetailViewTestCase, cls).setUpClass()
        User = get_user_model()
        cls.user = User.objects.create_user(username='test_user', password='134pass')
        Profile.objects.create(user=cls.user)
        cls.user.user_permissions.add(Permission.objects.get(codename='view_order'))

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

        self.test_order = Order.objects.create(
            buyer=self.user.profile,
            promo_code='test_code',
            address='test_address'
        )
        products1 = Product.objects.get(pk=7)
        products2 = Product.objects.get(pk=8)
        products3 = Product.objects.get(pk=9)
        self.test_order.save()
        self.test_order.products.add(products1, products2, products3)

    def test_order_detail(self):
        response = self.client.get(
            reverse('order_detail', kwargs={'pk': self.test_order.id})
        )
        self.assertContains(response, self.test_order.id)
        self.assertContains(response, self.test_order.address)
        self.assertContains(response, self.test_order.promo_code)
        self.assertEqual(response.context['object'].id, self.test_order.id)


class OrdersExportDataViewTestCase(TestCase):
    fixtures = [
        "products-fixture.json",
        "profile-fixture.json",
        'users-fixture.json',
        'order-fixture.json'
    ]

    @classmethod
    def setUpClass(cls):
        super(OrdersExportDataViewTestCase, cls).setUpClass()
        User = get_user_model()
        cls.user = User.objects.create_superuser(username='test_user', password='134pass')
        Profile.objects.create(user=cls.user)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_get_order_view(self):
        response = self.client.get(reverse('order_export'))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            response.headers['content-type'], 'application/json',

        )
        export_data = [
            {
                "pk": order.pk,
                "address": order.address,
                "promo_code": order.promo_code,
                'buyer': order.buyer.user.id,
                'products': [product.id for product in order.products.all()]

            }
            for order in Order.objects.all()
        ]

        orders_data = response.json()
        self.assertEqual(orders_data['orders'], export_data)
