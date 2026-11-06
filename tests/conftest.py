from pathlib import Path

import pytest


@pytest.fixture
def fixtures_dir():
    return Path(__file__).parent / "fixtures"


@pytest.fixture
def read_fixture(fixtures_dir):
    def read(name):
        return (fixtures_dir / name).read_text(encoding="utf-8").rstrip("\n")

    return read
