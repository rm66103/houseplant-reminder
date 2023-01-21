import factory

from .models import Account

class AccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Account
        django_get_or_create = ('email',)

    email = "test@test.com"
    phone = "1234567890"
    password = "foobar"
