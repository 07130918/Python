def example(param):
    """[Explain docstring]
    関数の説明はこのように書くのがpythonの習慣
    Args:
        params ([type]): [description]
        param ([str]): [stdout]
    Returns:
        bool: True
    """
    print(param)
    return True


example('docstringsの説明')
print(example.__doc__)
