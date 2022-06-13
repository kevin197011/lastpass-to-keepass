# Copyright (c) 2022 Operator
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import csv


class CSVUtil:

    @staticmethod
    def read_csv(file_path):
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            return list(reader)

    # csv_filepath = 'D:/DevOps/project/data/countries.csv'
    # data = ['title', 'username', 'password', 'url', 'notes']
    @staticmethod
    def write_csv(csv_filepath, data):
        with open(csv_filepath, 'w') as f:
            writer = csv.writer(f, delimiter=',', quotechar="'", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(data)