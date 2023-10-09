import unittest
from models.base import Base

class Test1Methods(unittest.TestCase):
    def test_id_assignment(self):
        # Test if the id is correctly assigned when provided
        obj = Base(1)
        self.assertEqual(obj.id, 1)

    def test_id_generation(self):
        # Testing si el id coincide
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_id_increment(self):
        # Test if the id is correctly incremented for each new instance
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)