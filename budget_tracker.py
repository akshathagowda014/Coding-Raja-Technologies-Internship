import os
import json

class BudgetTracker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.transactions = self.load_transactions()

    def load_transactions(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_transactions(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.transactions, file)

    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.save_transactions()

    def remove_transaction(self, index):
        self.transactions.pop(index)
        self.save_transactions()

    def mark_completed(self, index):
        self.transactions[index]['completed'] = True
        self.save_transactions()

    def list_transactions(self):
        for i, transaction in enumerate(self.transactions):
            print(f"{i}: {transaction['type']} - {transaction['category']} - {transaction['amount']}")

    def analyze_expenses(self):
        expenses_by_category = {}
        for transaction in self.transactions:
            if transaction['type'] == 'expense':
                if transaction['category'] in expenses_by_category:
                    expenses_by_category[transaction['category']] += transaction['amount']
                else:
                    expenses_by_category[transaction['category']] = transaction['amount']
        for category, amount in expenses_by_category.items():
            print(f"{category}: {amount}")

def main():
    budget_tracker = BudgetTracker('transactions.json')

    while True:
        print("\nTo-Do List Application")
        print("1: Add Transaction")
        print("2: Remove Transaction")
        print("3: Mark Completed")
        print("4: List Transactions")
        print("5: Analyze Expenses")
        print("6: Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            transaction_type = input("Enter transaction type (expense/income): ")
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            budget_tracker.add_transaction({'type': transaction_type, 'category': category, 'amount': amount, 'completed': False})
        elif choice == '2':
            index = int(input("Enter transaction index to remove: "))
            budget_tracker.remove_transaction(index)
        elif choice == '3':
            index = int(input("Enter transaction index to mark as completed: "))
            budget_tracker.mark_completed(index)
        elif choice == '4':
            budget_tracker.list_transactions()
        elif choice == '5':
            budget_tracker.analyze_expenses()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()