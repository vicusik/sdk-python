from datetime import date
import factory
from factory import fuzzy

CARDS = [
    '4111111111111111',
]


class CreditCard(factory.DictFactory):
    first_name = fuzzy.FuzzyText()
    last_name = fuzzy.FuzzyText()

    card_number = fuzzy.FuzzyChoice(choices=CARDS)
    expire_date = fuzzy.FuzzyDate(start_date=date.today())
    cvv = fuzzy.FuzzyText(length=3, chars='0123456789')
