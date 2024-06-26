import re

import pytest

import zipfile_inflate64 as zipfile


@pytest.fixture
def zip_file(data_dir):
    zip_path = data_dir / 'deflate64.zip'
    with zipfile.ZipFile(zip_path, mode='r') as zip_file:
        yield zip_file


@pytest.fixture(
    params=[
        '10_lines.txt',
        '100_lines.txt',
        '10k_lines.txt',
        '100k_lines.txt',
    ]
)
def file_name(request, zip_file):
    return request.param


@pytest.fixture
def zip_ext_file(zip_file, file_name):
    with zip_file.open(file_name, mode='r') as zip_ext_file:
        yield zip_ext_file


def test_zipfile_compress_type(zip_file):
    for zip_ext_file in zip_file.infolist():
        assert zip_ext_file.compress_type == zipfile.ZIP_DEFLATED64


def test_zipfile_extract(tmp_path, zip_file, file_name):
    zip_file.extract(file_name, path=tmp_path)
    assert (tmp_path / file_name).exists()


def test_zipfile_extractall(tmp_path, zip_file):
    zip_file.extractall(path=tmp_path)
    assert len(list(tmp_path.iterdir())) == 4


def test_zipfile_read(zip_ext_file):
    decompressed_content = zip_ext_file.read()
    assert decompressed_content


def test_zipfile_read_zero(zip_ext_file):
    decompressed_content = zip_ext_file.read(0)
    assert decompressed_content == b''


def test_zipfile_read_short(zip_ext_file):
    decompressed_content = zip_ext_file.read(18)
    assert decompressed_content == b'Sample content 0.\n'


def test_zipfile_readline_repeated(zip_ext_file):
    while True:
        decompressed_content = zip_ext_file.readline()
        if not decompressed_content:
            break
        assert re.match(rb'^Sample content \d+\.\n$', decompressed_content)


def test_zipfile_read_long(zip_file):
    with zip_file.open('100k_lines.txt', mode='r') as zip_ext_file:
        # Read an entire block
        zip_ext_file.read(64 << 10)
        # Read a little more, to the end of the line
        zip_ext_file.readline()
        # Read a whole line from the second block
        decompressed_content = zip_ext_file.readline()
    assert decompressed_content == b'Sample content 3174.\n'
