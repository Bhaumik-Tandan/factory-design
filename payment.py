"""
Payment Gateway Factory:
Create a PaymentGatewayFactory that generates different payment gateway objects (PayPal, Stripe, etc.) 
based on a user's chosen payment method.
"""

from abc import ABC, abstractmethod

class PaymentGatewayFactory(ABC):
    def __init__(self, email, password):
        self.email = email
        self.password = password

    @abstractmethod
    def display_info(self):
        pass


class PayPal(PaymentGatewayFactory):
    def display_info(self):
        print(f"This is a PayPal account with email {self.email} and password {self.password}")


class Stripe(PaymentGatewayFactory):
    def display_info(self):
        print(f"This is a Stripe account with email {self.email} and password {self.password}")


class Venmo(PaymentGatewayFactory):
    def display_info(self):
        print(f"This is a Venmo account with email {self.email} and password {self.password}")


def main():
    paypal = PayPal("username", "password")
    stripe = Stripe("username", "password")
    venmo = Venmo("username", "password")

    payment_gateways = [paypal, stripe, venmo]
    for payment_gateway in payment_gateways:
        payment_gateway.display_info()

if __name__ == "__main__":
    main()
