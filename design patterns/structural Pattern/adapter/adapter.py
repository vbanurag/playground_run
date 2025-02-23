class StripePayment:
    def make_payment(self, amount):
        print(f"Processing ${amount} payment via Stripe")


class PayPalPayment:
    def send_money(self, amount):
        print(f"Processing ${amount} payment via PayPal")

# Target Interface (Expected by the system)
class PaymentProcessor:
    def make_payment(self, amount):
        pass

# Adaptee (Existing Stripe Integration)
class StripePayment(PaymentProcessor):
    def make_payment(self, amount):
        print(f"Processing ${amount} payment via Stripe")

# Adapter for PayPal
class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal):
        self.paypal = paypal

    def make_payment(self, amount):
        # Adapting PayPal's `send_money()` to `make_payment()`
        self.paypal.send_money(amount)

# Client Code
if __name__ == "__main__":
    stripe = StripePayment()
    stripe.make_payment(100)

    paypal = PayPalPayment()
    adapter = PayPalAdapter(paypal)
    adapter.make_payment(200)  # Works with PayPal now!
