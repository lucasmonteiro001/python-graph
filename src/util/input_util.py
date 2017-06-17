"""This module contains the class responsible for dealing with the standard input"""
from sys import stdin


class InputUtil(object):
    """Class that contais function to read deal with standard input"""

    @staticmethod
    def read_standard_input():
        """
        Method that read line from standard input and return it as string
        :return: returns the read string from the standard input
        """

        try:
            print "Enter with the graph edges separated by comma: " \
                  "(e.g: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7)"

            user_input = stdin.readline()

            return user_input
        except Exception:
            raise Exception("Error reading standard input")
