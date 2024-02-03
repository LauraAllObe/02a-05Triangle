# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testInvalidInputA1(self):
        self.assertEqual(classifyTriangle(201,199,200), "InvalidInput", "201,199,200 is an Invalid Input")
    def testInvalidInputA2(self):
        self.assertEqual(classifyTriangle(199,201,200), "InvalidInput", "199,201,200 is an Invalid Input")
    def testInvalidInputA3(self):
        self.assertEqual(classifyTriangle(200,199,201), "InvalidInput", "200,199,201 is an Invalid Input")

    def testInvalidInputB1(self):
        self.assertEqual(classifyTriangle(0,199,200), "InvalidInput", "0,199,200 is an Invalid Input")
    def testInvalidInputB2(self):
        self.assertEqual(classifyTriangle(199,0,200), "InvalidInput", "199,0,200 is an Invalid Input")
    def testInvalidInputB3(self):
        self.assertEqual(classifyTriangle(200,199,0), "InvalidInput", "200,199,0 is an Invalid Input")

    def testInvalidInputC1(self):
        self.assertEqual(classifyTriangle(155.5,199,200), "InvalidInput", "155.5,199,200 is an Invalid Input") 
    def testInvalidInputC2(self):
        self.assertEqual(classifyTriangle(199,155.5,200), "InvalidInput", "199,155.5,200 is an Invalid Input") 
    def testInvalidInputC3(self):
        self.assertEqual(classifyTriangle(200,199,155.5), "InvalidInput", "200,199,155.5 is an Invalid Input") 

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(200,1,1), "NotATriangle", "200,1,1 is not a triangle")
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1,200,1), "NotATriangle", "1,200,1 is not a triangle")
    def testNotATriangleC(self):
        self.assertEqual(classifyTriangle(1,1,200), "NotATriangle", "1,1,200 is not a triangle")

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),"RightScalene",'3,4,5 is a Right triangle')
    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),"RightScalene",'5,3,4 is a Right triangle')
    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4,5,3),"RightScalene",'4,5,3 is a Right triangle')

    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(3,2,3),'Isoceles','3,2,3 is an Isoceles triangle')
    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(2,3,3),'Isoceles','2,3,3 is an Isoceles triangle')
    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(3,3,2),'Isoceles','3,3,2 is an Isoceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

