import csv
import os

class CsvInterface:
    def __init__(self, expenses, file_path):
        self.expenses = expenses
        self.file_path = file_path

    def write_csv(self):
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.expenses[0].keys())  # Create a CSV DictWriter
            writer.writeheader()  # Write the header (fieldnames)
            writer.writerows(self.expenses)  # Write the rows of data

    def load_csv(self):
        list_of_expenses = []
        
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", newline="") as file:
                reader = csv.reader(file)
                
                next(reader, None)  # Skip the header row
                
                for row in reader:
                    
                    list_of_expenses.append({
                        "date": row[0],
                        "category": row[1],
                        "amount": float(row[2]),  # Convert amount to float for calculations
                        "description": row[3]
                    })
        
        return list_of_expenses  # Properly indented return statement
