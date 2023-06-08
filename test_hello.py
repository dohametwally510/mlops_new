from hello import sum_xy


def test_sum_xy():
    assert 2 == sum_xy(1, 1)
    assert 4 == sum_xy(3,1 )
