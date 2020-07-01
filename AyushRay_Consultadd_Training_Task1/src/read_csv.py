import csv
import os


def reading():
    ROOT_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    CSV_PATH = ROOT_DIR + r'\\resources\Task_Training_Data .csv'
    data_list = []
    with open(CSV_PATH, 'r') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            data_list.append([row[0].strip(), row[1].strip()])

    return data_list
