from datetime import timedelta

from django.utils import timezone

import factory

from accounts.factories import AccountFactory

from .models import Plant

class PlantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Plant

    name = "example snake plant"
    account = factory.SubFactory(AccountFactory)
    last_watered = timezone.now()
    frequency = 7

    class Params:
        needs_water = factory.Trait(
            name = "dry snake plant",
            last_watered = timezone.now() - timedelta(days=8)
        )