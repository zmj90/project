# content of test_ids.py
import pytest


@pytest.fixture(params=[0, 1], ids=["spam", "ham"])
def a(request):
    return request.param


def test_a(a):
    pass


# def idfn(fixture_value):
#     if fixture_value == 0:
#         return "eggs"
#     else:
#         return None


def idfn(fv):
    return fv[1]


@pytest.fixture(params=[(1, "case.001"), (2, "case.002")], ids=idfn)
def b(request):
    return request.param


def test_b(b):
    pass
