"""Module responsible for printing utilities"""


class PrintUtil(object):
    """Class that contains function to print strings to standard output"""

    number = 0

    @staticmethod
    def print_string_to_standard_output(string, no_print=False):
        """
        Print a #string to the standard output follwing a format pattern and
        returns the formated string
        :param string: string to be printed
        :param no_print: If True, don't print the string tho the standard output. Else, print it
        :return: returns the formated string
        """

        PrintUtil.number += 1

        message = "Output #{}: {}".format(PrintUtil.number, str(string))

        if not no_print:
            print message + "\n"

        return message
