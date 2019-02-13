#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pcuf` package."""
import hashlib
import warnings

import pytest

import pcuf
from tests.utils import TEST_DIR


@pytest.fixture
def file(request):
    test_file = TEST_DIR / "foo.txt"
    content = "hello"

    with open(str(test_file), "w+") as f:
        f.write(content)

    file_hash = hashlib.sha1(test_file.read_bytes()).hexdigest()

    def teardown():
        if test_file.is_file():
            test_file.unlink()

    request.addfinalizer(teardown)
    return dict(file=test_file, content=content, hash=file_hash)


def test_file_hash(file):
    """Test pcuf.file.sha1"""
    file_hash = file["hash"]
    cal_hash = pcuf.file.sha1(file["file"])

    assert file_hash == cal_hash


def test_file_rename(file):
    """Test pcuf.file.rename"""
    renamed_file = TEST_DIR / "foobar.txt"

    assert file["file"].is_file()
    assert not renamed_file.is_file()

    pcuf.file.rename(file["file"], "foobar.txt")
    assert renamed_file.is_file()

    renamed_file.unlink()
    assert not renamed_file.is_file()


def test_deprecation_warning():
    """Tests pcuf.warnings.deprecate """

    with warnings.catch_warnings(record=True) as warns:
        # Cause all warnings to always be triggered.
        warnings.simplefilter("always")

        # Trigger deprecation warning.
        pcuf.warnings.deprecate(
            "Deprecation Test.",
            version=pcuf.__version__,
            link_uid="fhQbw",
            link_file="gist-test",
        )

        assert len(warns) == 1
        assert issubclass(warns[-1].category, DeprecationWarning)
        assert "Deprecation Test." in str(warns[-1].message)
        assert pcuf.__version__ in str(warns[-1].message)


def test_retry_function():
    """Tests pcuf.functions.retry"""

    def completes_on_third_call():
        if completes_on_third_call.state < 2:
            completes_on_third_call.state += 1
            raise TypeError

        return 1

    completes_on_third_call.state = 0
    value = pcuf.functions.retry(completes_on_third_call)

    assert completes_on_third_call.state == 2
    assert value == 1

    def always_fail():
        always_fail.state += 1
        raise TypeError

    always_fail.state = 0

    with pytest.raises(TypeError):
        pcuf.functions.retry(always_fail, retries=6)

    assert always_fail.state == 6
