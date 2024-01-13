import unittest
import os.path
from mymodule import send


class TestFtpSendFile(unittest.TestCase):

    def setUp(self):
        self.source_file_path = "/path/to/local/file.txt"
        self.dest_dir = "/path/to/remote/directory"
        self.dest_file_name = "file.txt"

    def test_send_success(self):
        result = send(self.source_file_path,
                               self.dest_dir, self.dest_file_name)
        self.assertTrue(result)

    def test_send_failure(self):
        # Remove the source file to trigger a failure
        os.remove(self.source_file_path)
        result = send(self.source_file_path,
                               self.dest_dir, self.dest_file_name)
        self.assertFalse(result)
