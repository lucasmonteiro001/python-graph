import unittest


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parses_correctly(self):
        self.assertEquals(1, 1, "ERRADO")

    def suite(self):
        tests = ['test_parses_correctly']

        return unittest.TestSuite(map(ParserTestCase, tests))