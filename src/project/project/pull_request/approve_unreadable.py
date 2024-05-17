def approve(lst):  # type:ignore
    """
    lstのデータの型が不明瞭かつ全ての型を入力に取れるようになっている (バグの原因)
    lstに第一要素があることを暗黙の前提としてしまっている (バグの原因)
    lstそもそもどのような要素を持っているのかがわからない
    何をapproveしているのかがわからない
    """
    res = lst
    res[1] = True

    return res
