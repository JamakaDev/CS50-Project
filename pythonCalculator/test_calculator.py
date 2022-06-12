import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

  def test_add(self):
    self.assertEqual(add(150, 450), 600.0)
    self.assertEqual(add(51, -1), 50.0)
    self.assertEqual(type(add(1, 2)), float)
  
  def test_subtract(self):
    self.assertEqual(subtract(150, 450), -300.0)
    self.assertEqual(subtract(51, -1), 52.0)
    self.assertEqual(type(subtract(1, 2)), float)
  
  def test_multiply(self):
    self.assertEqual(multiply(150, 450), 67500.0)
    self.assertEqual(multiply(51, -1), -51.0)
    self.assertEqual(type(multiply(1, 2)), float)

  def test_divide(self):
    self.assertEqual(divide(150, 450), 0.3333333333)
    self.assertEqual(divide(51, -1), -51.0)
    self.assertEqual(type(divide(1, 2)), float)

  def test_pos_neg(self):
    self.assertEqual(pos_neg(5), -5)
    self.assertEqual(pos_neg(-5), 5)
    self.assertEqual(type(pos_neg(5)), float)

  def test_clearThis(self):
    self.assertEqual(clearThis(), str())

  def test_clearAll(self):
    self.assertEqual(clearAll(), (str(), str()))
  
  def test_operation(self):
    self.assertEqual(operation('+', 10, 25), 35.0)
    self.assertEqual(operation('-', 10, 25), -15.0)
    self.assertEqual(operation('*', 10, 25), 250.0)
    self.assertEqual(operation('/', 10, 25), 0.4)

if __name__ == "__main__":
  unittest.main()