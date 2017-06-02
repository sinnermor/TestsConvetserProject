import os
import csv

def create_data_for_paranetrize():
    with open('param.csv') as csvfile:
        csv_data = csv.DictReader(csvfile)
        data = dict.fromkeys(['source', 'destination', 'exchange'])
        for row in csv_data:
            data = row
        return data

def test_fuct():
    print(create_data_for_paranetrize())