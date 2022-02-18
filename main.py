import pytest

"""
Тесты для структуры данных float
"""


def test_float_int_casting():
    assert 2 == int(2.2)
    assert -2 == int(-2.0)


def test_float():
    assert isinstance(23 / 4, float)
    assert isinstance(0 / 4, float)
    assert isinstance(-10 / 4, float)
    assert not isinstance(10 // 4, float)
    try:
        assert isinstance(float('sdf'), float)
    except ValueError:
        pass


@pytest.mark.parametrize("param, exp_out", [(32.0, True), ('sdf', False)])
def test_float_case(param, exp_out):
    assert isinstance(param, float) == exp_out


"""
Тесты для структуры данных dict
"""


def test_dict_empty_case():
    assert {} == dict()


def test_dict_catch_error():
    d = {'key': 'value'}

    assert d.get('key')
    assert d['key']
    assert not d.get('unknown_key')
    try:
        assert d['unknown_key']
    except KeyError:
        pass


@pytest.mark.parametrize("param, exp_out, ans", [
    ([['key1', 'value1'], ['key2', 'value2']],
     {'key1': 'value1', 'key2': 'value2'}, True),
    ([['key1', 'value'], ['key2', 'value2']],
     {'key7': 'value11', 'key23': 'value32'}, False)
])
class TestClass:
    def test_dict_case(self, param, exp_out, ans):
        new_dict = {}
        for elem in param:
            new_dict[elem[0]] = elem[1]

        eq = new_dict == exp_out
        assert eq == ans
