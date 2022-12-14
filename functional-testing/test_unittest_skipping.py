import sys
import unittest

class MyTestCase(unittest.TestCase):
    @unittest.skip("This is how to skip the test")
    def test_nothing(self):
        self.fail("This shouldnt display")
        
    @unittest.skipIf(sys.version_info.major < 3, "You are on Python version 2.0")
    def test_python_version(self):
        self.assertEqual("{}".format("Version 3"), "Version 3")
        pass
    
    @unittest.skipUnless(sys.platform.startswith("win"), "Only runs on windows")
    def test_computer_os(self):
        pass
    
    def test_skipped(self):
        
        if 1 == 1:
            self.skipTest("skip this test")
            

unittest.main(argv=[""], verbosity=2, exit= False)