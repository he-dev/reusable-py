import os

from daily_py.src.daily_py.files import temp_file


class TestTempFile:

    def test_file_created_by_default(self):
        with temp_file() as temp_name:
            assert os.path.isfile(temp_name)  # file created by default
        assert not os.path.isfile(temp_name)  # file deleted by default

    def test_file_not_created_when_disabled(self):
        with temp_file(create=False) as temp_name:
            assert not os.path.isfile(temp_name)  # file not created
        assert not os.path.isfile(temp_name)  # file deleted by default
