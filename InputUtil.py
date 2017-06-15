from sys import stdin


class InputUtil(object):
    @staticmethod
    def read_standard_input():
        try:
            print "Enter with the graph edges separated by comma: (e.g: AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7)"
            input = stdin.readline()
            return input
        except Exception:
            raise Exception("Error reading standard input")
