# Copyright (c) 2022 Operator
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# pip install pykeepass

from pykeepass import PyKeePass


class KeepassUtil:

    def __init__(self, keepass_file, keepass_password):
        self.keepass_file = keepass_file
        self.keepass_password = keepass_password

    def _open_keepass(self):
        return PyKeePass(self.keepass_file, self.keepass_password)

    def read_entries(self):
        kp = self._open_keepass()
        return kp.entries

    def write_keepass(self, groupname, data):
        kp = self._open_keepass()
        group = kp.find_groups(name=groupname, first=True)
        kp.add_entry(group, data[0], data[1], data[2], data[3], data[4])
        kp.save()

    def find_group(self, groupname):
        kp = self._open_keepass()
        ks = [g.name for g in kp.groups]
        return True if groupname in ks else False

    def add_group(self, groupname):
        kp = self._open_keepass()
        kp.add_group(kp.root_group, groupname)
        kp.save()
