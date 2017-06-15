from sys import stdin


class InputUtil(object):
    @staticmethod
    def read_standard_input():
        try:
            input = stdin.readline()
            return input
        except Exception:
            raise Exception("Error reading standard input")
