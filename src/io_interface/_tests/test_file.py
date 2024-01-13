import pytest
from my_module import export_files


@pytest.fixture()
def supplier():
    class MockSupplier:
        supplier_prefix = "mock_supplier"
        dir_exportECTORY = "/path/to/export/directory"

    return MockSupplier()


@pytest.fixture()
def data():
    return {"name": ["Alice", "Bob"], "age": [25, 30]}


def test_export_files_csv(supplier, data, tmp_path):
    file_format = "csv"
    file_name = "test_csv"
    file_path = tmp_path / \
        f"{supplier.supplier_prefix}_{file_name}.{file_format}"
    assert export_files(supplier, data, file_name, file_format)

    # Check that the file was created and contains the correct data
    with open(file_path, "r") as f:
        assert f.read() == "name;age\nAlice;25\nBob;30\n"


def test_export_files_json(supplier, data, tmp_path):
    file_format = "json"
    file_name = "test_json"
    file_path = tmp_path / \
        f"{supplier.supplier_prefix}_{file_name}.{file_format}"
    assert export_files(supplier, data, file_name, file_format)

    # Check that the file was created and contains the correct data
    with open(file_path, "r") as f:
        assert f.read() == '{"name": ["Alice", "Bob"], "age": [25, 30]}'


def test_export_files_txt(supplier, data, tmp_path):
    file_format = "txt"
    file_name = "test_txt"
    file_path = tmp_path / \
        f"{supplier.supplier_prefix}_{file_name}.{file_format}"
    assert export_files(supplier, data, file_name, file_format)

    # Check that the file was created and contains the correct data
    with open(file_path, "r") as f:
        assert f.read() == "{'name': ['Alice', 'Bob'], 'age': [25, 30]}"
