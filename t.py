# Copyright (c) 2022 Operator
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import config
from lib.csvUtil import CSVUtil
from pykeepass import PyKeePass


# kp = PyKeePass(config.keepass_file, config.keepass_password)

# # print(kp.groups)
# gp = kp.find_groups(name='M3', first=True)
# kp.add_entry(gp, 'title2', 'username', 'password', 'https://www.google.com','notes')
# kp.save()

data = ['title', 'username', 'password', 'url', 'notes']
# CSVUtil.write_csv(config.csv_filepath, data)
cr = CSVUtil.read_csv(config.csv_filepath)
print(cr)