from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    

class Paypal(PaymentStrategy):
    def pay(self, amount):
        print(f'Paying {amount} using Paypal')
        
class Razorpay(PaymentStrategy):
    def pay(self, amount):
        print(f'Paying {amount} using Razorpay')
        
        
class Stripe(PaymentStrategy):
    def pay(self, amount):
        print(f'Paying {amount} using Stripe')
        
class PaymentContext:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy
        
    def pay(self, amount):
        self.payment_strategy.pay(amount)
                
        
        
if __name__ == "__main__":
    # User selects Stripe as payment method
    context = PaymentContext(Stripe())
    context.execute_payment(100)

    # User switches to PayPal
    context.set_strategy(Paypal())
    context.execute_payment(200)

    # User switches to Razorpay
    context.set_strategy(Razorpay())
    context.execute_payment(300)
            
            
# Class Diagram:
# 
# +-------------------+       +-------------------+
# | PaymentStrategy   |<------+| PaymentContext   |
# +-------------------+       +-------------------+
# | + pay(amount)     |       | - payment_strategy|
# +-------------------+       +-------------------+
#        ^                        | + pay(amount)  |
#        |                        +----------------+
#        |
# +------+-------+-------+
# |              |       |
# |              |       |
# |              |       |
# +---------+    +---------+    +---------+
# | Paypal  |    | Razorpay|    | Stripe  |
# +---------+    +---------+    +---------+
# | + pay() |    | + pay() |    | + pay() |
# +---------+    +---------+    +---------+
