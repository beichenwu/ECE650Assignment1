import unittest
import support_functions

class TestStringMethods(unittest.TestCase):

    def test_street_input_analysis(self):
        self.assertEqual(support_functions.street_input_analysis('a "A" (2,3) (4,5)'),('"A"',[[2,3],[4,5]]))
        self.assertEqual(support_functions.street_input_analysis('c "B" (7,3) (4,5)'), ('"B"', [[7,3],[4,5]]))
        self.assertEqual(support_functions.street_input_analysis('r "C"'), ('"C"', []))



if __name__ == '__main__':
    unittest.main()