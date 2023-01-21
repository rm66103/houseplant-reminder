from datetime import timedelta
from unittest.mock import Mock

from django.test import TestCase
from django.utils import timezone

from accounts.factories import AccountFactory
from plants.factories import PlantFactory

class PlantTestCase(TestCase):
    def setUp(self):
        self.plant = PlantFactory.create()
        self.dry_plant = PlantFactory.create(needs_water=True)

    def test_save(self):
        self.plant.set_next_watering_on_create = Mock()
        self.plant.save()

        self.plant.set_next_watering_on_create.assert_called_once()

    def test_set_next_watering_on_create(self):
        self.plant.pk = None
        self.plant.next_watering = None

        self.plant.set_next_watering_on_create()

        self.assertNotEqual(self.plant.next_watering, None)

    def test_watering_interval_timedelta_class(self):
        self.assertEqual(self.plant.watering_interval_timedelta().__class__, timedelta)

    def test_watering_interval_timedelta_duration(self):
        self.assertEqual(self.plant.watering_interval_timedelta().days, self.plant.frequency)

    def test_next_watering_datetime(self):
        next_watering = self.plant.last_watered + self.plant.watering_interval_timedelta()
        self.assertEqual(self.plant.next_watering_datetime(), next_watering)
        
    def test_water_sets_last_watered(self):
        last_watered = self.plant.last_watered
        self.plant.water()

        self.assertGreater(self.plant.last_watered, last_watered)

    def test_water_calls_set_next_watering(self):
        self.dry_plant.set_next_watering = Mock()
        self.dry_plant.water()

        self.dry_plant.set_next_watering.assert_called_once()

    def test_needs_water(self):
        self.assertGreater(timezone.now(), self.dry_plant.next_watering_datetime())
        self.assertTrue(self.dry_plant.needs_water())

    def test_next_watering_is_out_of_date_false(self):
        self.assertFalse(self.plant.next_watering_is_out_of_date())

    def test_next_watering_is_out_of_date_true(self):
        self.plant.last_watered = timezone.now()
        self.assertTrue(self.plant.next_watering_is_out_of_date())

