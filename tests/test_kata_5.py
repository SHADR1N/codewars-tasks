from tasks import array_diff


def test_array_diff():
    assert array_diff([1, 2], [1]) == [2], "a was [1,2], b was [1], expected [2]"
    assert array_diff([1, 2, 2], [1]) == [2, 2], "a was [1,2,2], b was [1], expected [2,2]"
    assert array_diff([1, 2, 2], [2]) == [1], "a was [1,2,2], b was [2], expected [1]"
    assert array_diff([1, 2, 2], []) == [1, 2, 2], "a was [1,2,2], b was [], expected [1,2,2]"
    assert array_diff([], [1, 2]) == [], "a was [], b was [1,2], expected []"
    assert array_diff([1, 2, 3], [1, 2]) == [3], "a was [1,2,3], b was [1, 2], expected [3]"
