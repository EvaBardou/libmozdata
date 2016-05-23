# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

import unittest
from clouseau import hgmozilla
from clouseau.connection import Query


class RevisionTest(unittest.TestCase):

    def test_revision(self):
        rev = hgmozilla.Revision.get_revision()
        self.assertIsNot(rev, None)

    def test_revisions(self):
        data1 = {}
        data2 = {}

        def handler1(json, data):
            data.update(json)

        def handler2(json, data):
            data.update(json)

        hgmozilla.Revision(queries=[
            Query(hgmozilla.Revision.get_url('nightly'), {'node': 'tip'}, handler1, data1),
            Query(hgmozilla.Revision.get_url('nightly'), {'node': 'tip'}, handler2, data2),
        ]).wait()

        self.assertIsNot(data1, None)
        self.assertIsNot(data2, None)

class FileInfoTest(unittest.TestCase):

    def test_fileinfo(self):
        path = 'netwerk/protocol/http/nsHttpConnectionMgr.cpp'
        info = hgmozilla.FileInfo.get(path)

        self.assertIsNot(info, None)
        self.assertIsNot(info['netwerk/protocol/http/nsHttpConnectionMgr.cpp'], None)

    def test_fileinfo_multiple_files(self):
        paths = ['netwerk/protocol/http/nsHttpConnectionMgr.cpp', 'netwerk/protocol/http/nsHttpConnectionMgr.h']
        info = hgmozilla.FileInfo.get(paths)

        self.assertIsNot(info, None)
        self.assertIsNot(info['netwerk/protocol/http/nsHttpConnectionMgr.cpp'], None)
        self.assertIsNot(info['netwerk/protocol/http/nsHttpConnectionMgr.h'], None)

    def test_fileinfo_release_channel(self):
        path = 'netwerk/protocol/http/nsHttpConnectionMgr.cpp'
        info = hgmozilla.FileInfo.get(path, 'release')

        self.assertIsNot(info, None)
        self.assertIsNot(info['netwerk/protocol/http/nsHttpConnectionMgr.cpp'], None)


if __name__ == '__main__':
    unittest.main()
