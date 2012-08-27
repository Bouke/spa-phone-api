import unittest
import time

import spa_phone

test_ip = '10.0.1.8'
recovery_time = 9

class Test(unittest.TestCase):
    def test_a_backup(self):
        global backup
        backup = spa_phone.read(test_ip)

    def test_b_clear(self):
        spa_phone.write(test_ip, [])
        time.sleep(recovery_time)
        assert len(spa_phone.read(test_ip)) == 0

    def test_c_write(self):
        global backup
        spa_phone.write(test_ip, backup)
        time.sleep(recovery_time)
        assert spa_phone.read(test_ip) == backup

if __name__ == '__main__':
    unittest.main()
