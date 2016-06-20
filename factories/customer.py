from datetime import date
import factory
from factory import fuzzy


class CustomerFactory(factory.DictFactory):
    first_name = fuzzy.FuzzyText()
    last_name = fuzzy.FuzzyText()

    email = factory.LazyAttribute(lambda obj: '%s@test.local' % obj.first_name)
    ref_id = factory.Sequence(lambda n: "M-%s" % n)
