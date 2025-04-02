from expense_item import ExpenseItem

class ExpenseTracker:
  def __init__(self):
    self.history = []
    self.budget = 0

  def add_expense(self):
    self.history.append(ExpenseItem().details())

  def show_history(self):
    for index, item in enumerate(self.history):
      if (item["date"] and item["category"] and item["amount"] and item["description"]):
        print("Expense:", index + 1)
        print("  Date:", item["date"])
        print("  Cat:", item["category"])
        print("  Amount:", item["amount"])
        print("  Description:", item["description"])
      else:
        print("Expense:", index + 1, "- Information is missing")

  def set_budget(self):
    self.budget = int(input("Enter Monthly Budget:"))

  def calculate_expenses(self):
    total_expenses = 0
    for expense in self.history:
      total_expenses += expense["amount"]
    if (total_expenses < self.budget):
      print(f"You have {round((self.budget - total_expenses), 2)} left for the month")
    elif (total_expenses > self.budget):
      print("You have exceeded your budget!")
    else:
      print("You have reached your budget!")
  
  def write_to_csv(self, file_path = "expenses.csv"):
    ExpenseToCsv(self.history, file_path)
    self.history = [] #clear the history storage once it is written to csv to prevent duplicates