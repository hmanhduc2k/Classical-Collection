import unittest
from django.test import TestCase, Client
from django.test import RequestFactory
from django.urls import reverse
from django.shortcuts import render, redirect

from ..models import Piece, Composer, Period, Difficulty
from classcoll.utils import PieceSearch

PLACEHOLDER_FILE = "/upload/thisFileDoesNotExist.mp3"

class PieceTest(TestCase):
    def testPieces(self):
        c1 = Composer.objects.create(name="Wolfgang Amadeus Mozart")
        c2 = Composer.objects.create(name="Pyotr Ilyich Tchaikovsky")
        c3 = Composer.objects.create(name="Johann Sebastian Bach")
        c4 = Composer.objects.create(name="Frédéric François Chopin")
        c1.save()
        c2.save()
        c3.save()
        c4.save()
        
        p1 = Period.objects.create(era="Baroque")
        p1.save()
        p2 = Period.objects.create(era="Classical")
        p2.save()
        p3 = Period.objects.create(era="Romantic")
        p3.save()
        
        d1 = Difficulty.objects.create(rating="Easy")
        d1.save()
        d2 = Difficulty.objects.create(rating="Medium")
        d2.save()
        d3 = Difficulty.objects.create(rating="Difficult")
        d3.save()
        p1 = Piece.objects.create(
            name="Sonata no. 1",
            composer=Composer.objects.filter(name="Wolfgang Amadeus Mozart").first(),
            description="None",
            source=PLACEHOLDER_FILE,
            period=Period.objects.filter(era="Classical").first(),
            difficulty=Difficulty.objects.filter(rating="Medium").first()
        )
        p2 = Piece.objects.create(
            name="Partita no. 6",
            composer=Composer.objects.filter(name="Johann Sebastian Bach").first(),
            description="None",
            source=PLACEHOLDER_FILE,
            period=Period.objects.filter(era="Baroque").first(),
            difficulty=Difficulty.objects.filter(rating="Difficult").first()
        )
        p3 = Piece.objects.create(
            name="Ballade no. 4",
            composer=Composer.objects.filter(name="Frédéric François Chopin").first(),
            description="None",
            source=PLACEHOLDER_FILE,
            period=Period.objects.filter(era="Romantic").first(),
            difficulty=Difficulty.objects.filter(rating="Difficult").first()
        )
        p4 = Piece.objects.create(
            name="Waltz no. 19",
            composer=Composer.objects.filter(name="Frédéric François Chopin").first(),
            description="None",
            source=PLACEHOLDER_FILE,
            period=Period.objects.filter(era="Romantic").first(),
            difficulty=Difficulty.objects.filter(rating="Easy").first()
        )
        p1.save()
        p2.save()
        p3.save()
        p4.save()
        
        self.assertTrue(PieceSearch.match(p1, "Sonata", "Classical", "Medium"))
        self.assertFalse(PieceSearch.match(p1, "Sonata", "All", ""))
        self.assertTrue(PieceSearch.match(p2, "", "All", "Difficult"))
        self.assertTrue(PieceSearch.match(p2, "Partita", "Baroque", "All"))
        self.assertFalse(PieceSearch.match(p3, "Scherzo", "All", ""))
        self.assertFalse(PieceSearch.match(p3, "Valse", "Romantic", "Easy"))
        self.assertFalse(PieceSearch.match(p4, "", "", ""))
        self.assertTrue(PieceSearch.match(p4, "no. 19", "Romantic", "Easy"))