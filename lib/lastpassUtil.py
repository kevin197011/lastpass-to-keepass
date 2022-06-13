# Copyright (c) 2022 Operator
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

# pip install lastpass-python

import lastpass
from csvUtil import CSVUtil


class LastpassUtil:

    def __init__(self, lastpass_username, lastpass_password):
        self.lastpass_username = lastpass_username
        self.lastpass_password = lastpass_password

    def _open_lastpass(self):
        return lastpass.Vault.open_remote(self.lastpass_username, self.lastpass_password)

    def lastpass_to_csv(self, csv_filepath):
        CSVUtil.write_csv(csv_filepath, ['title', 'username', 'password', 'url', 'notes'])
        for row in self._open_lastpass().accounts:
            CSVUtil.write_csv(csv_filepath, [row.title, row.username, row.password, row.url, row.notes])
