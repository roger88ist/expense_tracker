from expense_tracker import ExpenseTracker
import sys

class Interface:
	def __init__(self):
		self.tracker = ExpenseTracker()

	def start(self):
		proceed = True

		while proceed:
			ipt = self.ask_for_input()

			match ipt:
				case "1":
					self.tracker.add_expense()
				case "2":
					self.tracker.show_history()
				case "3":
					self.tracker.set_budget()
					self.tracker.calculate_expenses()
				case "4":
					self.tracker.save_to_csv()
				case "5":
					proceed = False

	def ask_for_input(self):
		self.display_menu()
		return input("Enter Option: ")


	def display_menu(self):
		# self.clear_console()
		print("1. Add Expense")
		print("2. View Expenses")
		print("3. Track Budget")
		print("4. Save Expenses")
		print("5. Exit")

	def clear_console(self):
	    sys.stdout.write("\033[H\033[J")  # ANSI escape code to clear screen
	    sys.stdout.flush()


Interface().start()