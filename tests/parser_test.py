import unittest
from src.parser_util import ParserUtil


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parses_with_comma_correctly(self):
        line = ParserUtil.parse_string("AB7,TX14")

        edge1 = line[0]
        edge2 = line[1]

        self.assertEquals(len(line), 2, "Should have two edges")

        self.assertEquals(edge1.origin, "A")
        self.assertEquals(edge1.destination, "B")
        self.assertEquals(edge1.distance, 7)

        self.assertEquals(edge2.origin, "T")
        self.assertEquals(edge2.destination, "X")
        self.assertEquals(edge2.distance, 14)

    def test_parses_with_spaces_correctly(self):
        line = ParserUtil.parse_string("XZ99 HQ12")

        edge1 = line[0]
        edge2 = line[1]

        self.assertEquals(len(line), 2, "Should have two edges")

        self.assertTrue(edge1.origin == "X" and edge1.destination == "Z" and edge1.distance == 99)

        self.assertTrue(edge2.origin == "H" and edge2.destination == "Q" and edge2.distance == 12)

    def test_parses_with_comma_and_multiple_spaces_correctly(self):
        line = ParserUtil.parse_string("    VK8098   , HQ12       , VO1")

        edge1 = line[0]
        edge2 = line[1]
        edge3 = line[2]

        self.assertEquals(len(line), 3)

        self.assertTrue(edge1.origin == "V" and edge1.destination == "K" and edge1.distance == 8098)

        self.assertTrue(edge2.origin == "H" and edge2.destination == "Q" and edge2.distance == 12)

        self.assertTrue(edge3.origin == "V" and edge3.destination == "O" and edge3.distance == 1)
