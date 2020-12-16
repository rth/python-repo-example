from repo_example.base import add_int

def test_add_int():
    res = add_int(1, 2)
    assert res == 3
