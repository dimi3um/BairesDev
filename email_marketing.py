class EmailMarketing:

    def __init__(self, in_file, rcalc):
        self.in_file = in_file
        with open(self.in_file) as file:
            self.data = [rcalc.rate(x[:-1].split('|')) for x in file.readlines()]

    def get(self, out_file, quantity):
        with open(out_file, 'wt') as file:
            [file.write(x['id']+'\n') for x in self.data[:quantity]]