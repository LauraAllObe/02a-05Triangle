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
    """For testing triangles and the various test cases that are aimed at,
    providing optimal working of the triangle program"""
    def test_invalid_input_a1(self):
        """Triangles with sides greater than 200 are invalid"""
        self.assertEqual(classifyTriangle(201,199,200),
                         "InvalidInput",
                         "201,199,200 is an Invalid Input")
    def test_invalid_input_a2(self):
        """Triangles with sides greater than 200 are invalid"""
        self.assertEqual(classifyTriangle(199,201,200),
                         "InvalidInput",
                         "199,201,200 is an Invalid Input")
    def test_invalid_input_a3(self):
        """Triangles with sides greater than 200 are invalid"""
        self.assertEqual(classifyTriangle(200,199,201),
                         "InvalidInput",
                         "200,199,201 is an Invalid Input")
    def test_invalid_input_b1(self):
        """Triangles cannot be formed with side 0"""
        self.assertEqual(classifyTriangle(0,199,200),
                         "InvalidInput",
                         "0,199,200 is an Invalid Input")
    def test_invalid_input_b2(self):
        """Triangles cannot be formed with side 0"""
        self.assertEqual(classifyTriangle(199,0,200),
                         "InvalidInput",
                         "199,0,200 is an Invalid Input")
    def test_invalid_input_b3(self):
        """Triangles cannot be formed with side 0"""
        self.assertEqual(classifyTriangle(200,199,0),
                         "InvalidInput",
                         "200,199,0 is an Invalid Input")
    def test_invalid_input_c1(self):
        """Triangles cannot be formed with sides greater than 200"""
        self.assertEqual(classifyTriangle(155.5,199,200),
                         "InvalidInput",
                         "155.5,199,200 is an Invalid Input")
    def test_invalid_input_c2(self):
        """Triangles cannot be formed with sides greater than 200"""
        self.assertEqual(classifyTriangle(199,155.5,200),
                         "InvalidInput",
                         "199,155.5,200 is an Invalid Input")
    def test_invalid_input_c3(self):
        """Triangles cannot be formed with sides greater than 200"""
        self.assertEqual(classifyTriangle(200,199,155.5),
                         "InvalidInput",
                         "200,199,155.5 is an Invalid Input")
    def test_not_a_triangle_a(self):
        """Cannot be a triangle as length of one side is greater than 200"""
        self.assertEqual(classifyTriangle(200,1,1),
                         "NotATriangle",
                         "200,1,1 is not a triangle")
    def test_not_a_triangle_b(self):
        """Cannot be a triangle as length of one side is greater than 200"""
        self.assertEqual(classifyTriangle(1,200,1),
                         "NotATriangle",
                         "1,200,1 is not a triangle")
    def test_not_a_triangle_c(self):
        """Cannot be a triangle as length of one side is greater than 200"""
        self.assertEqual(classifyTriangle(1,1,200),
                         "NotATriangle",
                         "1,1,200 is not a triangle")
    def test_right_triangle_a(self):
        """This test case Verifies that the triangle is a right triangle"""
        self.assertEqual(classifyTriangle(3,4,5),
                         "RightScalene",
                         '3,4,5 is a Right triangle')
    def test_right_triangle_b(self):
        """This test case Verifies that the triangle is a right triangle"""
        self.assertEqual(classifyTriangle(5,3,4),
                         "RightScalene",
                         '5,3,4 is a Right triangle')
    def test_right_triangle_c(self):
        """This test case Verifies that the triangle is a right triangle"""
        self.assertEqual(classifyTriangle(4,5,3),
                         "RightScalene",
                         '4,5,3 is a Right triangle')
    def test_equilateral_triangles(self):
        """This test case Verifies that the triangle is an equilateral triangle"""
        self.assertEqual(classifyTriangle(1,1,1),
                         'Equilateral',
                         '1,1,1 should be equilateral')
    def test_isoceles_triangle_a(self):
        """This test case Verifies that the triangle is an isoceles triangle"""
        self.assertEqual(classifyTriangle(3,2,3),
                         'Isoceles',
                         '3,2,3 is an Isoceles triangle')
    def test_isoceles_triangle_b(self):
        """This test case Verifies that the triangle is an isoceles triangle"""
        self.assertEqual(classifyTriangle(2,3,3),
                         'Isoceles',
                         '2,3,3 is an Isoceles triangle')
    def test_isoceles_triangle_c(self):
        """This test case Verifies that the triangle is an isoceles triangle"""
        self.assertEqual(classifyTriangle(3,3,2),
                         'Isoceles',
                         '3,3,2 is an Isoceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
