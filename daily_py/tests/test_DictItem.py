import pytest

from daily_py.src.daily_py.collections import DictItem, DictExpected, NotExtendable


def test_can_set_item():
    data = DictItem({"foo": {"bar": {"baz": "baz"}}})
    data["foo/bar/baz"] = "qux"
    assert data.source == {"foo": {"bar": {"baz": "qux"}}}


def test_can_append_branches():
    data = DictItem({"foo": {"bar": {"baz": "baz"}}})
    data["foo/bar/qux"] = "qux"
    assert data.source == {"foo": {"bar": {"baz": "baz", "qux": "qux"}}}


def test_can_create_branches_deep():
    data = DictItem({}, extendable=True)
    data["foo/bar/qux"] = "qux"
    assert data.source == {"foo": {"bar": {"qux": "qux"}}}


def test_stops_when_new_branches_disallowed():
    data = DictItem({"foo": {}})
    with pytest.raises(NotExtendable, match="Cannot create branch at 'foo/bar'."):
        data["foo/bar/qux"] = "qux"


def test_stops_when_key_is_not_dict():
    data = DictItem({"foo": {"bar": "baz"}})
    with pytest.raises(DictExpected, match="Path at 'foo/bar' is not a dictionary."):
        data["foo/bar/qux"] = "qux"
