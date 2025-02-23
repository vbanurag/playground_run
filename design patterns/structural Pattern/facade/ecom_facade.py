'''
    Your eCommerce platform has multiple subsystems for handling customer inquiries:

    Order Tracking → Fetch order status.
    Returns & Refunds → Process return requests.
    Support Tickets → Log customer complaints.
    Live Chat Assistance → Connect to a chatbot or human agent.

'''

class OrderTracking:
    def fetch_order_status(self, order_id):
        return f"Order #{order_id} is currently in transit."
    
class ReturnsRefunds:
    def process_return_request(self, order_id):
        return f"Return request for order #{order_id} has been processed."

class SupportTickets:
    def log_complaint(self, customer_id, complaint):
        return f"Complaint from customer #{customer_id} has been logged: {complaint}"


class LiveChatAssistance:

    def connect_to_chatbot(self):
        return "Connecting to chatbot..."
    
    def connect_to_human_agent(self):
        return "Connecting to human agent..."


class CustomerSupportFacade:

    def __init__(self):
        self.order_tracking = OrderTracking()
        self.returns_refunds = ReturnsRefunds()
        self.support_tickets = SupportTickets()
        self.live_chat = LiveChatAssistance()

    def get_order_status(self, order_id):
        return self.order_tracking.fetch_order_status(order_id)

    def process_return(self, order_id):
        return self.returns_refunds.process_return_request(order_id)

    def log_complaint(self, customer_id, complaint):
        return self.support_tickets.log_complaint(customer_id, complaint)

    def connect_to_chatbot(self):
        return self.live_chat.connect_to_chatbot()

    def connect_to_human_agent(self):
        return self.live_chat.connect_to_human_agent()  


# Usage 
if __name__ == "__main__":
    customer_support = CustomerSupportFacade()
    print(customer_support.get_order_status(12345))  # Order #12345 is currently in transit.
    print(customer_support.process_return(12345))  # Return request for order #12345 has been processed.
    print(customer_support.log_complaint(12345, "I received a damaged product."))  # Complaint from customer #12345 has been logged: I received a damaged product.
    print(customer_support.connect_to_chatbot())  # Connecting to chatbot...
    print(customer_support.connect_to_human_agent())  # Connecting to human agent...




    