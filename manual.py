import os.path
import csv


def put_data(data):
    filename = 'data.csv'
    file_exists = os.path.isfile(filename)
    with open(filename, 'a') as csvfile:
        headers = ['ball','run']
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=headers)

        if not file_exists:
            writer.writeheader()  # file doesn't exist yet, write a header

        writer.writerow(data)
    csvfile.close()
