from django.db import models
from datetime import datetime
from django.utils.timezone import now

class Event(models.Model):
    title = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    list_date = models.DateTimeField(default=now, blank=True)

    class Meta:
        verbose_name_plural = "events"

    def __str__(self):
        return self.title







































# class Event(models.Model):
#     class StateChoice(models.TextChoices):
#         Alabama = "Alabama, AL"
#         Alaska = "Alaska, AK"
#         Arizona = "Arizona, AZ"
#         Arkansas = "Arkansas, AR"
#         California = "California, CA"
#         Colorado = "Colorado, CO"
#         Connecticut = "Connecticut, CT"
#         Delaware = "Delaware, DE"
#         Tennesse = "Tennesse, TN"
#         Texas = "Texas, TX"
#         Utah = "Utah, UT"
#         Vermont = "Vermont, VT"
#         Virginia = "Virginia, VA"
#         Washington = "Washington, WA"
#         West_virginia = "West_virginia, WT"
#         Wisconsin = "Wisconsin, WI"
#         Wyoming = "Wyoming, WY"

#     title = models.CharField(max_length=50)
#     place = models.CharField(max_length=50)
#     city = models.CharField(max_length=10)
#     state = models.CharField(
#         max_length=50, choices=StateChoice.choices, default=StateChoice.Alabama
#     )
#     zipcode = models.CharField(max_length=10)
#     other = models.CharField(max_length=50)
#     start_date = models.CharField(max_length=25)
#     end_date = models.CharField(max_length=25)
#     category = models.CharField(max_length=25)
#     list_date = models.DateTimeField(default=now, blank=True)

#     class Meta:
#         verbose_name_plural = "events"

#     def __str__(self):
#         return self.title
