import sys

class Config:

    def __init__(self, cli_args):
        self.parse_arguments(cli_args)

    def parse_arguments(self, cli_args):
        try:
            self.katalet_name = cli_args[0]
        except:
            print 'Please enter a katalet name and format [human|json]'
            exit(2)
        try:
            self.out_format = cli_args[1]
        except:
            self.out_format = 'human'

class Katalet:

    def __init__(self, katalet_name):
        self.katalet_name = katalet_name

    def print_name(self, out_format):
        if out_format == 'human':
            return self.human_format(self.katalet_name)
        elif out_format == 'json':
            return self.json_format(self.katalet_name)

    def human_format(self, text):
        return 'The katalet you have selected is %s.' % text

    def json_format(self, text):
        return '{ name: "%s" }' % text

def main(argv):
    config = Config(argv)
    katalet = Katalet(config.katalet_name)
    print katalet.print_name(config.out_format)

if __name__ == "__main__":
        main(sys.argv[1:])
