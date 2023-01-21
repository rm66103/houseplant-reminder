from datetime import timedelta

from django.db import models
from django.utils import timezone

class Plant(models.Model):
    account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    last_watered = models.DateTimeField()
    next_watering = models.DateTimeField()
    frequency = models.IntegerField() # watered once per X days

    def save(self, *args, **kwargs):
        self.set_next_watering_on_create()

        super(Plant, self).save(*args, **kwargs)

    def set_next_watering_on_create(self):
        if self.pk == None: # pk will be None only during the intial create!
            self.next_watering = self.next_watering_datetime()

    def watering_interval_timedelta(self):
        return timedelta(days=self.frequency)

    def next_watering_datetime(self):
        return self.last_watered + self.watering_interval_timedelta()

    def water(self):
        self.last_watered = timezone.now()
        self.set_next_watering()
        self.save()

    def needs_water(self):
        return timezone.now() > self.next_watering_datetime()

    def next_watering_is_out_of_date(self):
        """
        The `next_watering` property is "out of date" when
        the plant gets watered. This will update the `last_watered`
        date which will update the return of `next_watering_datetime`.

        This check is how we know when we want to update `.next_watering`
        in the db.
        """
        return self.next_watering != self.next_watering_datetime()

    def set_next_watering(self):
        """
        This model sets the `.next_watering` property.
        Note that it does not save!
        """
        self.next_watering = self.next_watering_datetime()
    