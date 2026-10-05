from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} processed using Credit Card.")

class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} processed using Debit Card.")

class UPI(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} processed using UPI.")

class NetBanking(PaymentStrategy):
    def pay(self, amount):
        print(f"Payment of ${amount} processed using Net Banking.")


class PaymentProcessor:
    def __init__(self, strategy= None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy =  strategy

    def pay(self, amount): 
        if self.strategy is None:
            print("please select payment method")

        else:
            self.strategy.pay(amount)



payment_method = PaymentProcessor()


while True:
    Choice = input("""Enter Payment Method 
                1. Credit Card
                2. Debit Card
                3. UPI
                4. Net Banking
                5. Exit \n """
                   )
    if Choice == "5":
        print("exit")
        break

    if Choice == "1":
        payment_method.set_strategy(CreditCardPayment())
    elif Choice == "2":
        payment_method.set_strategy(DebitCardPayment())
    elif Choice == "3":
        payment_method.set_strategy(UPI())
    elif Choice == "4":
        payment_method.set_strategy(NetBanking())
    else:
        print("invalid choice")
        continue

    try:
        amount = float(input("Enter the amount to be paid: "))
    except ValueError:
        print("Invalid amount")
        continue

    payment_method.pay(amount)


#     Enter Payment Method 
#                 1. Credit Card
#                 2. Debit Card
#                 3. UPI
#                 4. Net Banking
#                 5. Exit 
#  2
# Enter the amount to be paid: 456
# Payment of $456.0 processed using Debit Card.
# Enter Payment Method 
#                 1. Credit Card
#                 2. Debit Card
#                 3. UPI
#                 4. Net Banking
#                 5. Exit 
#  3
# Enter the amount to be paid: 7896
# Payment of $7896.0 processed using UPI.
# Enter Payment Method 
#                 1. Credit Card
#                 2. Debit Card
#                 3. UPI
#                 4. Net Banking
#                 5. Exit 
#  4
# Enter the amount to be paid: 5689
# Payment of $5689.0 processed using Net Banking.
# Enter Payment Method 
#                 1. Credit Card
#                 2. Debit Card
#                 3. UPI
#                 4. Net Banking
#                 5. Exit 
#  5
# exit
