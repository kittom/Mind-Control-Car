
from csv import writer, reader


class FileManager:
    def __init__(self):
        self.csv = "/Users/morgan/Desktop/Mind-Control-Car/BrainWaveReader/dataLogs/data.csv"

    def get_dt(self):
        with open(self.csv, "r", newline='') as file:

            csv_reader = reader(file)
            data = list()
            for row in reversed(list(csv_reader)):
                try:
                    return row[0]
                except IndexError:
                    pass
            # data.append(csv_reader[len(csv_reader)-1][0])
            return data

    def add_dt(self, _dt):

        # print(self.path)
        with open(self.csv, 'a', newline='') as file:
            csv_writer = writer(file)
            row = [_dt]
            csv_writer.writerow(row)
            return True

if __name__ == "__main__":

    fm = FileManager()

    print(fm.get_dt())

