from email_marketing import EmailMarketing
from rate_calculator import RateCalculator


def main():
    calculator = RateCalculator()
    clients = EmailMarketing('people.in', calculator)
    clients.data.sort(key=lambda x: x['rate'], reverse=True)
    clients.get('people.out', 100)


if __name__ == "__main__":
    main()
    print('Information has been processed successfully')
