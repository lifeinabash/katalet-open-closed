import sys

class Katalet:

    def __init__(self):

    def print_name(self, out_format):
        if out_format == 'human':
            return self.human_format(out_format)
        elif out_format == 'json':
            return self.json_format(out_format)

    def human_format(self, text):
        return 'The format you have selected is %s.' % text

    def json_format(self, text):
        return '{ format: "%s" }' % text

def main(argv):
    try:
        out_format = argv[1]
    except:
        print 'Please enter output format [human|json].'
        exit(2)

    katalet = Katalet()
    print katalet.print_name(out_format)

if __name__ == "__main__":
        main(sys.argv[1:])
