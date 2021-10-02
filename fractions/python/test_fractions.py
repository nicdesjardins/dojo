import pytest

from nfractions import nFraction, AddFractions

class TestnFraction(object):
    
    @pytest.mark.parametrize(
        "operation, expected",
        [
            ("1/2 + 3/4", [[1, 2], [3, 4]]),
            ("1/2 + 3/5", [[1, 2], [3, 5]]),
            ("1/2 + 4/5", [[1, 2], [4, 5]]),
            ("1/2 + 5/5", [[1, 2], [5, 5]]),
            ("10/20 + 5/5", [[10, 20], [5, 5]]),
        ]
    )
    def test_that_fraction_interpretation_is_correct(self, operation, expected):
        af = AddFractions(operation)
        af.parseOperation()
        for key, fraction in enumerate(af.fractions):
            assert fraction == expected[key]
    
    @pytest.mark.parametrize(
        "fraction, expected",
        [
            ([10, 20], [1, 2]),
            ([3, 6], [1, 2]),
            ([12, 24], [1, 2]),
            ([4, 6], [2, 3]),
            ([6, 8], [3, 4]),
            ([10, 32], [5, 16]),
            ([5, 2], [5, 2]),
        ]
    )
    def test_fraction_converts_to_lowest_common_fraction(self, fraction, expected):
        af = AddFractions('')
        lowest = af.lowestFraction(fraction)
        assert lowest == expected

if __name__ == "__main__":
    pytest.main(["-v"])