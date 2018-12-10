import unittest

# confirm that functions complain when there are too many or not enough fields

def comma_file():


def pipe_file():


def space_file():


class Output1Test(unittest.TestCase):
    def test_line(self):
        self.assertEqual(comma_file(3), 4)
