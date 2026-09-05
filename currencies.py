# pylint: disable=missing-docstring

# TODO: add some currency rates
RATES = {"USDEUR": 0.85, "GBPEUR": 1.13, "CHFEUR": 0.86}

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    value, foreign_currency = amount

    if foreign_currency == currency:
        return value

    rate_to_eur = RATES.get(foreign_currency + "EUR")
    if rate_to_eur is not None and currency == "EUR":
        value_2 = (rate_to_eur * value)
        return round(value_2)

    rate_from_eur = RATES.get(currency + "EUR")
    if foreign_currency == "EUR":
        value_3 = (value / rate_from_eur)
        return round(value_3)

    return None
