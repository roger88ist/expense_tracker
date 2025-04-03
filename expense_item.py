class ExpenseItem:
  def __init__(self):
    self.ask_for_date()
    self.ask_for_category()
    self.ask_for_price()
    self.ask_for_description()

  def ask_for_date(self):
    self.date = input("Enter Date (YYYY-MM-DD): ")

  def ask_for_category(self):
    self.category = input("Enter Expense Category: ")

  def ask_for_price(self):
    self.price = float(input("Enter Expense Amount: $"))

  def ask_for_description(self):
    self.description = input("Enter Description: ")

  def details(self):
    return {"date": self.date, "category": self.category, "amount": self.price, "description": self.description}