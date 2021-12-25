from django.test import TestCase
from .models import *
# Create your tests here.

class UserTestCase(TestCase):
    def setup(self):
        u1 = User.objects.create(username='username1', password='123456')
        u2 = User.objects.create(username='username2', password='fkoecb')
    
    def testUser(self):
        u1 = User.objects.create(username='username1', password='123456')
        self.assertEqual(u1.username, 'username1')