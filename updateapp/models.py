from django.db import models
from django.contrib.auth.models import User

class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length =30)
    location = models.CharField(max_length =50)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User)

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        neighborhood = cls.objects.get(id=neighborhood_id)
        return neighborhood

class User(models.Model):
    name = models.CharField(max_length =30)
    neighborhood = models.ForeignKey(Neighborhood)
    email = models.EmailField()

class Business(models.Model):
    business_name = models.CharField(max_length =50)
    user = models.ForeignKey(User)
    neighborhood = models.ForeignKey(Neighborhood)
    business_email = models.EmailField()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        business = cls.objects.get(id=business_id)
        return business

class Update(models.Model):
    title = models.CharField(max_length =30)
    description = models.TextField(max_length = 100)

    def save_update(self):
        self.save()

    def delete_update(self):
        self.delete()

    @classmethod
    def get_all(cls):
        updates = cls.objects.all()
        return updates
