import csv
import os

class CsvInterface:
  def __init__(self, expenses, file_path):
    self.expenses = expenses
    self.file_path = file_path

  def write_csv(self):
    if os.path.exists(self.file_path):
      # append to file
      mode = 'a'
    else:
      # write to file
      mode = 'b'

    with open(self.file_path, mode = mode, newline='') as file:
      if (mode == 'w'):
        writer = csv.DictWriter(file, fieldnames=self.expenses[0].keys()) # Create a CSV DictWriter
        writer.writeheader() # Write the header (fieldnames)
      else:
        writer.writerows(self.expenses) # Write the rows of data