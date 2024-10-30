from mymodule import mymodule

def test_top_n():
    """
    make sure top_n works
    """

    assert mymodule.top_n([8,3,2,7,4], 3) == [8,7,4], 'Incorrect'