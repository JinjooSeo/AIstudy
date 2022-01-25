import csv

class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self, file_path = ""):
        file_path = self.file_path
        csv_file = open(file_path, "r", encoding="utf8")
        reader = csv.reader(csv_file)
        data = list(reader)
        return data
    

file_path = "./data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.read_file())