import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
        print(1+2)
        print("This is another print statement")


if __name__ == '__main__':
    unittest.main()
