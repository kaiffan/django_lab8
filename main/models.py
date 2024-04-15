from datetime import datetime
from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(null=False)
    date_registration = models.DateTimeField(db_default=datetime.utcnow())


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(null=False)
    age = models.IntegerField(null=False)
    city = models.CharField(max_length=100, null=False)
    date_add = models.DateTimeField(db_default=datetime.utcnow())


class Subscription(models.Model):
    subscriber = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
    subscribed_to = models.ForeignKey(User, related_name='subscribers', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('subscriber', 'subscribed_to')