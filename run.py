# Copyright (c) 2022 Operator
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import config
from lib.keepassUtil import KeepassUtil
from lib.csvUtil import CSVUtil

groupname = 'M1'
data = CSVUtil.read_csv(config.csv_filepath)

kp = KeepassUtil(config.keepass_filepath, config.keepass_password)

# not exist group will be created
if not kp.find_group(groupname):
    kp.add_group(groupname)

for dt in data[1:]:
    # if dt
    if not len(dt):
        continue
    kp.write_keepass(groupname, dt)
print('Write data to keepass finish')
