from abc import ABC, abstractmethod

# Step 1: Define an abstract PaymentMethod class
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Step 2: Concrete Payment Implementations
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} via Credit Card."

class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        return f"Paid ${amount} via PayPal."

# Step 3: Factory Class
class PaymentFactory:
    @staticmethod
    def get_payment_method(method):
        payments = {
            "creditcard": CreditCardPayment(),
            "paypal": PayPalPayment(),
        }
        return payments.get(method.lower(), None)

# Step 4: Client Code (Using the Factory)
if __name__ == "__main__":
    factory = PaymentFactory()
    
    payment1 = factory.get_payment_method("creditcard")
    print(payment1.pay(100) if payment1 else "Invalid Payment Method")

    payment2 = factory.get_payment_method("paypal")
    print(payment2.pay(200) if payment2 else "Invalid Payment Method")


    # Class Diagram
    # 
    # +-------------------+
    # | PaymentMethod     |
    # +-------------------+
    # | + pay(amount)     |
    # +-------------------+
    #          ^
    #          |
    # +-------------------+       +-------------------+
    # | CreditCardPayment |       | PayPalPayment     |
    # +-------------------+       +-------------------+
    # | + pay(amount)     |       | + pay(amount)     |
    # +-------------------+       +-------------------+
    # 
    # +-------------------+
    # | PaymentFactory    |
    # +-------------------+
    # | + get_payment_method(method) |
    # +-------------------+
    # 
    # 
    # PaymentFactory -- creates --> PaymentMethod
    # PaymentMethod -- implemented by --> CreditCardPayment
    # PaymentMethod -- implemented by --> PayPalPayment
    # PaymentFactory -- uses --> CreditCardPayment
    # PaymentFactory -- uses --> PayPalPayment