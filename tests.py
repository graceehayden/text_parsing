import unittest
from parse import *

class TestParsing(unittest.TestCase):

    def test_output_1(self):
        """
        Make sure a parsed line looks as expected
        """
        output = parse_text()
        output_1 = output['output_1']

        self.assertIsInstance(output_1, list)
        self.assertEqual(output_1[0],'Hingis Martina Female 4/2/1979 Green')


    def test_output_2(self):
        """
        Make sure a parsed line looks as expected
        """
        output = parse_text()
        output_2 = output['output_2']

        self.assertIsInstance(output_2, list)
        self.assertEqual(output_2[0],'Abercrombie Neil Male 2/13/1943 Tan')


    def test_output_3(self):
        """
        Make sure a parsed line looks as expected
        """
        output = parse_text()
        output_3 = output['output_3']

        self.assertIsInstance(output_3, list)
        self.assertIsInstance(output_3[3], str)

        self.assertEqual(output_3[0],'Smith Steve Male 3/3/1985 Red')


    def test_written_output(self):
        output = parse_text()
        with open('ouput.txt') as text_1, open('target_output.txt') as text_2:
            for line1, line2 in zip(text_1, text_2):
                self.assertEqual(line1, line2)


if __name__ == '__main__':
    unittest.main()
