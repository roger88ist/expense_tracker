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
      mode = 'w'

    with open(self.file_path, mode=mode, newline='') as file:
      writer = csv.DictWriter(file, fieldnames=self.expenses[0].keys()) # Create a CSV DictWriter
      if (mode == 'w'):
        writer.writeheader() # Write the header (fieldnames)

      writer.writerows(self.expenses) # Write the rows of data