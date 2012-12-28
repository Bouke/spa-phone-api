import unittest
import time
from spa_api import read, write

import spa_phone

test_ip = '10.0.1.8'
recovery_time = 9

class Test(unittest.TestCase):
    def test_a_backup(self):
        global backup
        backup = read(test_ip)

    def test_b_clear(self):
        write(test_ip, [])
        time.sleep(recovery_time)
        assert len(read(test_ip)) == 0

    def test_c_write(self):
        global backup
        write(test_ip, backup)
        time.sleep(recovery_time)
        assert read(test_ip) == backup

if __name__ == '__main__':
    unittest.main()
