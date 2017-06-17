import unittest

from src.util.print_util import PrintUtil

MESSAGE = "DEFAULT MESSAGE TO BE PRINT"


def get_message(number, msg):
    return "Output #" + str(number) + ": " + msg


class PrintUtilTestCase(unittest.TestCase):
    def test_print_order(self):
        self.assertEquals(PrintUtil.print_string_to_standard_output(MESSAGE, True), get_message(1, MESSAGE))
        self.assertEquals(PrintUtil.print_string_to_standard_output(MESSAGE, True), get_message(2, MESSAGE))
        self.assertEquals(PrintUtil.print_string_to_standard_output(MESSAGE, True), get_message(3, MESSAGE))
        self.assertEquals(PrintUtil.print_string_to_standard_output(MESSAGE, True), get_message(4, MESSAGE))
        self.assertEquals(PrintUtil.print_string_to_standard_output(MESSAGE, True), get_message(5, MESSAGE))
