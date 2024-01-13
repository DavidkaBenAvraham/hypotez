import unittest
from unittest.mock import MagicMock, patch
import sys
sys.path.insert(0, '../')
from main import Thread4Supplier,start_script

class TestThread4Supplier(unittest.TestCase):
    
    def test_supplier_created_successfully(self):
        # Test that a Supplier instance is created successfully within the thread
        thread = Thread4Supplier(supplier_prefix="some_prefix", lang=["EN"])
        self.assertIsNotNone(thread.supplier)
        self.assertIsInstance(thread.supplier, Supplier)

    def test_thread_starts_and_runs_successfully(self):
        # Test that the thread starts and runs successfully
        thread = Thread4Supplier(supplier_prefix="some_prefix", lang=["EN"])
        self.assertIsNone(thread.supplier.status)  # Check that the status is initially None
        thread.start()
        thread.join()
        self.assertIsNotNone(thread.supplier.status)  # Check that the status is not None after running the thread

class TestStartScript(unittest.TestCase):
    def test_gui_mode(self):
        # Test GUI mode

        result = launcher(suppliers=['SUP1'], window_mode='window')
        self.assertTrue(result)

    def test_jupyter_mode(self):
        # Test jupyter mode

        result = launcher(window_mode='jupyter')
        self.assertTrue(result)

    def test_cmd_mode(self):
        # Test CMD mode

        result = launcher(window_mode='cmd')
        self.assertIsNone(result)

    def test_suppliers_list(self):
        # Test suppliers list

        result = launcher(suppliers=['aliexpress', 'morlevi'], window_mode='window')
        self.assertTrue(result)

    def test_scenario_list(self):
        # Test scenario list

        result = launcher(suppliers=['amazon'], scenario=['SCENARIO1', 'SCENARIO2'], window_mode='window')
        self.assertTrue(result)

    def test_language_list(self):
        # Test language list

        result = launcher(suppliers=['ksp'], lang=['EN', 'HE'], window_mode='window')
        self.assertTrue(result)

    def test_no_arguments(self):
        # Test with no arguments

        result = launcher()
        self.assertTrue(result)
