"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from core.models import Branch

class SimpleTest(TestCase):     
    def test_get_fields(self):    
        branch = Branch(name = "test",
                        adress = "test address",
                        phone = "000",
                        email = "test@email.com")                          
        fields = branch.get_fields()
        self.assertTrue(fields)
