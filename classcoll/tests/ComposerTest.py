import unittest
from django.test import TestCase, Client
from django.test import RequestFactory
from django.urls import reverse
from django.shortcuts import render, redirect

from ..models import Composer
from classcoll.utils import ComposerSearch

class TestSearchUtil(TestCase):
    def testComposerSearch(self):
        c1 = Composer.objects.create(name="Wolfgang Amadeus Mozart")
        c2 = Composer.objects.create(name="Pyotr Ilyich Tchaikovsky")
        c3 = Composer.objects.create(name="Johann Sebastian Bach")
        c4 = Composer.objects.create(name="Frédéric François Chopin")
        c1.save()
        c2.save()
        c3.save()
        c4.save()
        
        composer1 = Composer.objects.filter(name="Wolfgang Amadeus Mozart").first()
        self.assertEqual(ComposerSearch.search("Wolfgang Amadeus Mozart"), composer1)
        composer2 = Composer.objects.filter(name="Pyotr Ilyich Tchaikovsky").first()
        self.assertEqual(ComposerSearch.search("Peter Ilyich Tchaikovsky"), composer2)
        composer3 = Composer.objects.filter(name="Johann Sebastian Bach").first()
        self.assertNotEqual(ComposerSearch.search("Johann Christoph Bach"), composer3)
        composer4 = Composer.objects.filter(name="Frédéric François Chopin").first()
        self.assertEqual(ComposerSearch.search("Frederic Francois Chopin"), composer4)
        self.assertNotEqual(ComposerSearch.search("Nicholas Chopin"), composer4)