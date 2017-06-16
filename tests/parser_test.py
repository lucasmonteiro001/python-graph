import unittest
from src.ParserUtil import ParserUtil


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parses_correctly(self):

        line = ParserUtil.parse_line("AB7, TX14")

        edge1 = line[0]
        edge2 = line[1]

        self.assertEquals(len(line), 2, "Should have two edges")

        self.assertEquals(edge1.origin, "A")
        self.assertEquals(edge1.destination, "B")
        self.assertEquals(edge1.distance, 7)

        self.assertEquals(edge2.origin, "T")
        self.assertEquals(edge2.destination, "X")
        self.assertEquals(edge2.distance, 14)

