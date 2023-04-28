# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 09:52:01 2022

@author: Hitesh Maan
"""

from rearrange import rearrange
import unittest 

class rearrange_test(unittest.TestCase):
    def test_basic(self):
        testCase="Maan, Hitesh"
        expected="Hitesh Maan"
        self.assertEqual(rearrange(testCase), expected)
    def test_empty(self):
        testCase=""
        expected=""
        self.assertEqual(rearrange(testCase),expected)
    def test_doubleName(self):
        testCase="Maan, Gurdeep S."
        expected="Gurdeep S. Maan"
        self.assertEqual(rearrange(testCase),expected)
    def test_oneName(self):
        testCase="Harsimran"
        expected="Harsimran"
        self.assertEqual(rearrange(testCase),expected)
        
unittest.main()