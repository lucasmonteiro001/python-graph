from Edge import Edge


class ParserUtil(object):
    @staticmethod
    def __parse(element):
        return Edge(element[0], element[1], element[2:])

    @staticmethod
    def parse_line(line):
        # Token responsible for the parse
        token = ","

        # remove trailing/leading/repeated spaces before parsing
        return map(ParserUtil.__parse, " ".join(line.split(token)).split())
