""" Pytest tests for the dumb algorithm in max_substrings_split_1593 """
import pytest

from max_substrings_split_1593.dumb import max_unique_split


class TestDumbMaxUniqueSplit:
    """ Tests for the dumb algorithm in max_substrings_split_1593 """

    @pytest.mark.parametrize(
        's, expected',
        [
            ('ababccc', 5),
            ('aba', 2),
            ('aa', 1),
            ('a', 1),
            ('', 0),
            ('abc', 3),
            ('abac', 3),
            ('abacab', 4),
            ('abacaba', 4),
            ('abacabad', 5),
        ],
    )
    def test_max_unique_split(self, s, expected):
        assert max_unique_split(s) == expected
