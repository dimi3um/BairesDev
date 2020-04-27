class RateCalculator:

    def __init__(self):
        with open('./keywords/role.txt') as file:
            self.role = [x[:-1] for x in file.readlines()]
        with open('./keywords/country.txt') as file:
            self.country = [x[:-1] for x in file.readlines()]
        with open('./keywords/industry.txt') as file:
            self.industry = [x[:-1] for x in file.readlines()]

    @staticmethod
    def has_keyword(word, keyword_list):
        for keyword in keyword_list:
            return keyword in word
        return False

    def rate(self, fields):
        rr = self.has_keyword(fields[3].lower(), self.role)            # role rate
        cr = self.has_keyword(fields[4].lower(), self.country)         # country rate
        ir = self.has_keyword(fields[5].lower(), self.industry)        # industry rate
        con_r = int(fields[7])                          # connection rate

        # calculate recommendation rate
        rec_r = int(fields[6])/int(fields[7]) if int(fields[7]) > 0 else 0

        return {'rate': (rr, rec_r, con_r, ir, cr), 'id': fields[0]}
