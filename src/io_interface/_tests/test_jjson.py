import unittest
import json
from pathlib import Path
from jjson import json_loads, json_dump, html2json


class TestJsonLoad(unittest.TestCase):

    def setUp(self):
        self.data = {'key': 'value'}
        self.json_path = 'test.json'
        with open(self.json_path, 'w') as f:
            json.dump(self.data, f)

    def tearDown(self):
        Path(self.json_path).unlink()

    def test_load_from_file(self):
        result = json_loads(Path(self.json_path))
        self.assertEqual(result, self.data)

    def test_load_from_string(self):
        result = json_loads(json.dumps(self.data))
        self.assertEqual(result, self.data)

    def test_load_invalid_file(self):
        result = json_loads('invalid_file_path.json')
        self.assertFalse(result)


class TestJsonDump(unittest.TestCase):

    def setUp(self):
        self.data = {'key': 'value'}
        self.json_path = 'test.json'

    def tearDown(self):
        Path(self.json_path).unlink()

    def test_dump_to_file(self):
        result = json_dump(self.data, Path(self.json_path))
        self.assertTrue(result)
        with open(self.json_path, 'r') as f:
            loaded_data = json.load(f)
        self.assertEqual(loaded_data, self.data)

    def test_dump_invalid_file(self):
        result = json_dump(self.data, 'invalid_file_path.json')
        self.assertFalse(result)


class TestHtml2Json(unittest.TestCase):

    def setUp(self):
        self.html = '<html><body><h1>Test</h1></body></html>'

    def test_html2json(self):
        result = html2json(self.html)
        self.assertEqual(json.loads(result)['html'], self.html)


if __name__ == '__main__':
    unittest.main()
