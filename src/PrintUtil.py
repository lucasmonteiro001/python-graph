class PrintUtil(object):
    number = 0

    @staticmethod
    def print_output_test(arg, no_print=False):
        PrintUtil.number += 1

        message = "Output #{}: {}".format(PrintUtil.number, str(arg))

        if not no_print:
            print message + "\n"

        return message
