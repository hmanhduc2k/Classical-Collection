import unittest
from django.test import TestCase, Client
from django.test import RequestFactory
from django.urls import reverse
from django.shortcuts import render, redirect

from ..models import User
from classcoll.utils import PasswordStrength
from classcoll.views import Authentication

# Unit Test
class UserTest(TestCase):
    def testUserCreate(self):
        u1 = User.objects.create(username="Manh Duc", password="hmanhduc2k")
        self.assertEqual(u1.username, "Manh Duc")
        self.assertEqual(u1.password, "hmanhduc2k")
        self.assertNotEqual(u1.username, "Duc Manh")
        self.assertNotEqual(u1.password, "hmanhduck2")
    
    def testUserChange(self):
        u1 = User.objects.create(username="Manh Duc", password="hmanhduc2k")
        self.assertEqual(u1.username, "Manh Duc")
        u1.username = "Duc Minh"
        self.assertEqual(u1.username, "Duc Minh")
        self.assertNotEqual(u1.username, "Manh Duc")
        
class PasswordStrengthTest(TestCase):
    def testMinLength(self):
        u1 = User.objects.create(username="Manh Duc", password="hmanhduc")
        self.assertTrue(PasswordStrength.minLength(u1.password))
        u1.password = "manhduc"
        self.assertFalse(PasswordStrength.minLength(u1.password))
        u1.password = "3"
        self.assertFalse(PasswordStrength.minLength(u1.password))
        u1.password = "hmanhduc2klatentoi"
        self.assertTrue(PasswordStrength.minLength(u1.password))
        
    def testMinDistinct(self):
        u1 = User.objects.create(username="ManhDucHoang", password="hmanhduc2k")
        self.assertTrue(PasswordStrength.minDifference(u1.password, u1.username))
        u1.password = "ManhDucHoang"
        self.assertFalse(PasswordStrength.minDifference(u1.password, u1.username))
        u1.password = "ManhDucHuang"
        self.assertFalse(PasswordStrength.minDifference(u1.password, u1.username))
    
    def testMinComplex(self):
        u1 = User.objects.create(username="ManhDucHoang", password="hmanhduc2k")
        self.assertFalse(PasswordStrength.minComplex(u1.password))
        u1.password = "hmanhduc2k!"
        self.assertTrue(PasswordStrength.minComplex(u1.password))
        u1.password = "@#(*%)@)#$"
        self.assertFalse(PasswordStrength.minComplex(u1.password))
        u1.password = "fgoj3-23(#$#$"
        self.assertTrue(PasswordStrength.minComplex(u1.password))
