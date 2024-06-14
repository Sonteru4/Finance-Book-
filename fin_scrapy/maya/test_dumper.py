import unittest
import dumper

class MyTestCase(unittest.TestCase):
    def test_something(self):
        file_path = "data/convert.json"
        dumper.Dumper(file_path)
        #self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
