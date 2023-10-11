import unittest
from models.rectangle import Rectangle  # Import the Rectangle class from your module

class testRectangle(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 1)

    def test_area(self):
        r = Rectangle(4, 6)
        self.assertEqual(r.area(), 24)

    def test_display(self):
        r = Rectangle(2, 2)
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r.display()
            self.assertEqual(mock_stdout.getvalue(), "\n\n  ##\n  ##\n")

    def test_str(self):
        r = Rectangle(3, 4, 1, 1, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 1/1 - 3/4")

    def test_update(self):
        r = Rectangle(3, 4, 1, 1, 5)
        r.update(7, 2, 2, 0, 0)
        self.assertEqual(str(r), "[Rectangle] (7) 0/0 - 2/2")

    def test_to_dictionary(self):
        r = Rectangle(3, 4, 1, 1, 5)
        self.assertEqual(r.to_dictionary(), {'x': 1, 'y': 1, 'id': 5, 'width': 3, 'height': 4})

if __name__ == '__main__':
    unittest.main()
