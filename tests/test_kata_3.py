import re
import pytest

from tasks import regex


def do_test(string: str, expected: bool):
    actual = bool(re.fullmatch(regex, string))
    assert actual is expected, f'for string "{string}"'


@pytest.mark.parametrize("dataset", [
        ('ghdfj32', False),
        ('DSJKHD23', False),
        ('dsF43', False),
        ('4fdg5Fj3', True),
        ('DHSJdhjsU', False),
        ('fjd3IR9.;', False),
        ('fjd3  IR9', False),
        ('djI38D55', True),
        ('a2.d412', False),
        ('JHD5FJ53', False),
        ('!fdjn345', False),
        ('jfkdfj3j', False),
        ('123', False),
        ('abc', False),
        ('123abcABC', True),
        ('ABC123abc', True),
        ('Password123', True),
])
def test_regex(dataset):
    string, expected = dataset
    do_test(string, expected)

