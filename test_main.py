import unittest
from main import *

class TestMain(unittest.TestCase):
    def setUp(self):
        self.monitor = Monitor()

    def test_crear_interfaz(self):
        self.monitor.crear_interfaz()
        # TODO: Add assertions to verify the creation of the interface

if __name__ == '__main__':
    unittest.main()