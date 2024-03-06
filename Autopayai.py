import time
import random
import string

class Billy:
    def __init__(self):
        pass

    def ask_user_prompt(self):
        return input("Billy: How can I help you today? ")

    def process_prompt(self, user_prompt):
        if "due" in user_prompt.lower():
            print("Billy: Checking for your dues...")
            time.sleep(2)  # Simulating processing time
            self.show_dues()
            return True
        else:
            print("Billy: How can I assist you today?")
            return False

    def show_dues(self):
        # Simulated retrieval of dues from a database or external system
        dues = {"Electricity bill": 100, "Internet bill": 50, "Phone bill": 75}
        total_due = sum(dues.values())
        print("Billy: Here are your dues:")
        for due, cost in dues.items():
            print(f"- {due}: INR {cost}")
        print(f"Total dues: INR {total_due}")
        return dues

    def generate_transaction_id(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def process_payment(self, selected_due, dues):
        user_input = input("Billy: Do you want to pay this due? (yes/no): ").lower()
        if user_input == "yes":
            payment_method = input("Billy: Please select a payment method (credit card/bank/upi): ").lower()
            if payment_method == "credit card":
                card_number = input("Billy: Please enter your credit card number: ")
                expiry_date = input("Billy: Please enter the expiry date (MM/YY): ")
                cvv = input("Billy: Please enter the CVV: ")
                print("Billy: Processing payment with credit card...")
            elif payment_method == "bank":
                account_name = input("Billy: Please enter your account holder name: ")
                account_number = input("Billy: Please enter your bank account number: ")
                ifsc_code = input("Billy: Please enter the IFSC code: ")
                print("Billy: Processing payment via bank transfer...")
            elif payment_method == "upi":
                from_upi = input("Billy: Please enter your UPI ID: ")  # Sender's UPI ID
                to_upi = input("Billy: Please enter the recipient's UPI ID: ")
                print("Billy: Processing payment via UPI...")
            else:
                print("Billy: Invalid payment method selected.")
                return

            print(f"Billy: Starting payment process for {selected_due}...")
            print("Billy: Processing payment...")
            time.sleep(3)  # Simulating payment process
            print("Billy: Payment successful!")
            transaction_id = self.generate_transaction_id()
            print(f"Billy: Payment details - Due: {selected_due}, Amount: INR {dues[selected_due]}, "
                  f"Transaction ID: {transaction_id}, Payment Method: {payment_method}")
            if payment_method == "bank":
                print("Billy: Bank Account Details - Account Holder Name:", account_name,
                      "Account Number:", account_number, "IFSC Code:", ifsc_code)
            elif payment_method == "upi":
                print("Billy: UPI Transaction Details - Transaction ID:", transaction_id,
                      "From:", from_upi, "To:", to_upi)
            self.save_transaction_details(selected_due, dues[selected_due], transaction_id, payment_method,
                                          account_name if payment_method == "bank" else None,
                                          account_number if payment_method == "bank" else None,
                                          ifsc_code if payment_method == "bank" else None,
                                          from_upi if payment_method == "upi" else None,
                                          to_upi if payment_method == "upi" else None)
        elif user_input == "no":
            print("Billy: Okay, let me know if you need anything else.")
        else:
            raise ValueError("Invalid input. Please enter 'yes' or 'no'.")

    def save_transaction_details(self, due_name, amount, transaction_id, payment_method, account_name=None,
                                 account_number=None, ifsc_code=None, from_upi=None, to_upi=None):
        # Simulated saving of transaction details to a database or external system
        with open("transaction_details.txt", "a") as file:
            file.write("Payment Details:\n")
            file.write(f"Due: {due_name}, Amount: INR {amount}\n")
            file.write(f"Transaction ID: {transaction_id}, Payment Method: {payment_method}\n")
            if payment_method == "bank":
                file.write(f"Bank Account Details - Account Holder Name: {account_name}, "
                           f"Account Number: {account_number}, IFSC Code: {ifsc_code}\n")
            elif payment_method == "upi":
                file.write(f"UPI Transaction Details - Transaction ID: {transaction_id}, "
                           f"From: {from_upi}, To: {to_upi}\n")
            file.write("\n")

# Example usage:
if __name__ == "__main__":
    billy = Billy()
    while True:
        user_prompt = billy.ask_user_prompt()
        if user_prompt.lower() == "exit":
            break
        elif billy.process_prompt(user_prompt):
            dues = billy.show_dues()
            selected_due = input("Billy: Please select the due you want to pay: ")
            billy.process_payment(selected_due, dues)
