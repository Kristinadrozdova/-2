from main_vladimir import avg30_avg60, unsurv


def test_avg30_avg60():
    data = ['0,1,0,,0,0,0,20',
            '0,1,0,0,0,0,80',
            '0,1,0,,0,0,0,20',
            '0,1,0,,0,0,0,20',
            '0,1,0,,0,0,0,20']
    assert avg30_avg60(data) == (1, 4)


def test_unsurv():
    data = ['0,1,0,,0,0,0,20',
            '0,1,0,0,0,0,80',
            '0,1,0,,0,0,0,20',
            '0,1,0,,0,0,0,20',
            '0,1,0,,0,0,0,20']
    assert unsurv(data) == (0, 0)
