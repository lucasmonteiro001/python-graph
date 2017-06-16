class PrintUtil(object):
    number = 0

    @staticmethod
    def print_output_test(arg):
        PrintUtil.number += 1
        print "Output #{}: {}".format(PrintUtil.number, str(arg))
