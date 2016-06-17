import factory
from factory import fuzzy


class OrderFactory(factory.DictFactory):
    invoice_number = fuzzy.FuzzyInteger(low=1)
    description = fuzzy.FuzzyText()
    amount = fuzzy.FuzzyDecimal(low=1)
    ref_id = fuzzy.FuzzyText()
