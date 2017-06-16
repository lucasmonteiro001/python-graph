import unittest
from src.PrintUtil import PrintUtil

MESSAGE = "DEFAULT MESSAGE TO BE PRINT"


def get_message(number, msg):
    return "Output #" + str(number) + ": " + msg


class PrintUtilTestCase(unittest.TestCase):
    def test_print_order(self):
        self.assertEquals(PrintUtil.print_output_test(MESSAGE, True), get_message(1, MESSAGE))
        self.assertEquals(PrintUtil.print_output_test(MESSAGE, True), get_message(2, MESSAGE))
        self.assertEquals(PrintUtil.print_output_test(MESSAGE, True), get_message(3, MESSAGE))
        self.assertEquals(PrintUtil.print_output_test(MESSAGE, True), get_message(4, MESSAGE))
        self.assertEquals(PrintUtil.print_output_test(MESSAGE, True), get_message(5, MESSAGE))
