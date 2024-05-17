import pytest

from project.pull_request.approve_unreadable import approve


def test_approve() -> None:
    lst = [1, False]
    res = approve(lst=lst)
    assert res == [1, True]


def test_approve_raise_error_with_invalid_input() -> None:
    """
    第一要素がない場合にIndexErrorが発生する
    しかし、このエラーを見たところで何が起きているのかがわからない
    なぜなら、「lst」のindexがout of rangeであることはわかるが、
    それが何を意味しているのかが不明だからである
    """
    lst = [1]
    with pytest.raises(IndexError):
        approve(lst=lst)


def test_approve_has_bug_long_list() -> None:
    """
    approve関数をよく見るとValidationがないので、明らかにおかしな入力でも動く
    """
    lst = [1, False, False]
    res = approve(lst=lst)
    assert res == [1, True, False]


def test_approve_has_bug_invalid_type() -> None:
    """
    approve関数をよく見るとValidationがないので、明らかにおかしな入力でも動く
    """
    lst = [True, "hoge"]
    res = approve(lst=lst)
    assert res == [True, True]
