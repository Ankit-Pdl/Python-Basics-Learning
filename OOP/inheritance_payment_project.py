from abc import ABC, abstractmethod

# parent class
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    def validate_amount(self):
        if self.amount <= 0:
            raise ValueError("Payment amount must be greater than zero")

    @abstractmethod
    def pay(self):
        pass


class CreditCardPayment(Payment):
    def __init__(self, amount, card_number):
        super().__init__(amount)
        self.card_number = card_number

    def pay(self):
        self.validate_amount()
        print(f"Rs.{self.amount} paid using Credit Card ending with {self.card_number[-4:]}")


class NepalPayPayment(Payment):
    def __init__(self, amount, nepallink_id):
        super().__init__(amount)
        self.nepallink_id = nepallink_id

    def pay(self):
        self.validate_amount()
        print(f"Rs.{self.amount} paid using NepalPay ID: {self.nepallink_id}")


class CashPayment(Payment):
    def pay(self):
        self.validate_amount()
        print(f"Rs.{self.amount} paid in cash")



def main():
    payments = [
        CreditCardPayment(2500, "1234567890123456"),
        NepalPayPayment(1800, "NPAY-ANKIT-001"),
        CashPayment(700)
    ]

    for payment in payments:
        payment.pay()


if __name__ == "__main__":
    main()
