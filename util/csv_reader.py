import csv
from model.quote import Quote

class CsvReader:
    
    @staticmethod
    def read_quotes(filename:str):
        """Reads all quotes (including optional author) from the given CSV file and returns an array of Quote objects
        """
        with open(filename) as csv_file:
            quotes = []
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                q = Quote()
                try:
                    q.text = row[0].strip()
                    # Optional author
                    if row[1]:
                        q.author = row[1].strip()
                except IndexError:
                    # Optional author was not set, just skip then
                    pass
                quotes.append(q)
        return quotes
                