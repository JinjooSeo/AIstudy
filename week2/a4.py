import csv

class ReadCSV():
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self, file_path = ""):
        file_path = self.file_path
        csv_file = open(file_path, "r", encoding="utf8")
        reader = csv.reader(csv_file)
        file_data = list(reader)
        file_data = [list(map(int, comp)) for comp in file_data]
        return file_data

    def merge_list(self, file_data = ""):
        file_data = self.read_file()
        merge_data = [sum(i) for i in file_data]
        return merge_data
    

file_path = "./data-01-test-score.csv"
read_csv = ReadCSV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())