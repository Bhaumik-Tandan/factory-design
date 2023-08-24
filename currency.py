"""
* Currency Converter Factory:
* 		Create a CurrencyConverterFactory that produces currency converters for different currency pairs (USD to EUR, EUR to GBP).
"""

class CurrencyConverterFactory:

    def createCurrencyConverter(self, currencyPair):
        if currencyPair == "USD to EUR":
            return USDtoEURConverter()
        elif currencyPair == "EUR to GBP":
            return EURtoGBPConverter()
        else:
            return None

class USDtoEURConverter:
    def convert(self, amount):
        return amount * 0.82

class EURtoGBPConverter:
    def convert(self, amount):
        return amount * 0.86

def main():
    factory = CurrencyConverterFactory()

    usdToEurConverter = factory.createCurrencyConverter("USD to EUR")
    eurToGbpConverter = factory.createCurrencyConverter("EUR to GBP")

    amount = 100
    print("USD to EUR: " + str(usdToEurConverter.convert(amount)))
    print("EUR to GBP: " + str(eurToGbpConverter.convert(amount)))

if __name__ == "__main__":
    main()

    