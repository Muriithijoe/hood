from django.db import models
from django.contrib.auth.models import User

class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length =30)
    location = models.CharField(max_length =50)
    occupants = models.IntegerField()

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        neighborhood = cls.objects.get(id=neighborhood_id)
        return neighborhood

class UserProfile(models.Models):
    name = models.CharField(max_length =30)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null = True)
    email = models.EmailField()

class Business(models.Models):
    business_name = models.CharField(max_length =50)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE,null = True)
    business_email = models.EmailField()

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        business = cls.objects.get(id=business_id)
        return business
