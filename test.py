import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
        print("The tests are running")


if __name__ == '__main__':
    unittest.main()
