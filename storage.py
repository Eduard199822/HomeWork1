import csv

class Persistor:

   
    def __init__ (self, file_name,csv_file = ""):
        self.file_name = file_name
        self.csv_file = csv_file

    def read_raw_data(self):
        f = open(self.file_name,"r")
        return f.read()

    
    def save_raw_data(self, data):
        f = open(self.file_name,"w+")
        f.write(data)
    
    def save_csv(self, data):
        file = open(self.csv_file,"w+")
        writer = csv.DictWriter(file, fieldnames=["Country_Name", "Total Cases", "Total Deaths", "Total Recovered", "Active Cases"])
        writer.writeheader()
        for item in data:
            file.write(str(item) + '\n')

    def append_data(self, data):
        pass

        return f'{self.date} , {self.time} , {self.place} , {self.teamName} , {self.scored} , {self.missed}'
        file.write(str(d) + '\n')