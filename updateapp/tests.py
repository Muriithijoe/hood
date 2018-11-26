from django.test import TestCase
from .models import Neighborhood,UserProfile, Business

# Create your tests here.

class NeighborhoodTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_neighborhood =Neighborhood(name="tarek",location="Nairobi",count = "2")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighborhood,Neighborhood))

    #Testing Save Method
    def test_save_method(self):
        self.new_neighborhood.save_neighborhood()
        neighborhood=Neighborhood.objects.all()
        self.assertTrue(len(neighborhood)>0)

    def test_delete_method(self):
        self.new_neighborhood.save_neighborhood()
        self.new_neighborhood.delete_neighborhood()

    def test_update_neighborhood(self):
        self.new_neighborhood.save_neighborhood()
        self.new_neighborhood = Neighborhood.objects.get(id = 3 )
        self.new_neighborhood.update_neighborhood('Nairobi')
        self.updated_neighborhood = Neighborhood.objects.get(id = 3)
        self.assertEqual(self.updated_neighborhood.location,"Nairobi")

    def test_update_neighborhood(self):
        self.new_neighborhood.save_neighborhood()
        self.new_neighborhood = Neighborhood.objects.get(id = 3 )
        self.new_neighborhood.update_neighborhood('2')
        self.updated_neighborhood = Neighborhood.objects.get(id = 3)
        self.assertEqual(self.updated_neighborhood.count,2)

class UserStatusTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_userstatus =UserStatus(user_image="tarek.jpeg",user_email = "tarickaliabdi@gmail.com")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_userstatus,UserStatus))

    #Testing Save Method
    def test_save_method(self):
        self.new_userstatus.save_userstatus()
        userstatus = UserStatus.objects.all()https://github.com/shureim/Update-Neighbourhood
        self.assertTrue(len(userstatus)>0)

    def test_delete_method(self):
        self.new_userstatus.save_userstatus()
        self.new_userstatus.delete_userstatus()

class BusinessTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_business =Business(business_name="shopkeeper",business_email = "tarickaliabdi@gmail.com")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_business,Business))

    #Testing Save Method
    def test_save_method(self):
        self.new_business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business)>0)

    def test_delete_method(self):
        self.new_business.save_business()
        self.new_business.delete_business()

    def test_update_business(self):
        self.new_business.save_business()
        self.new_business= Business.objects.get(id = 3 )
        self.new_business.update_business('shopkeeper')
        self.updated_business = Business.objects.get(id = 3)
        self.assertEqual(self.updated_business.business_name,"shopkeeper")
