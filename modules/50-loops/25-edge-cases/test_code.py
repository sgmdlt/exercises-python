import index

def test1():
    string = 'Sansa Stark'
    end = len(string) - 1
    assert index.is_arguments_for_substr_correct(string, -1, 0) == False
    assert index.is_arguments_for_substr_correct(string, 0, -1) == False
    assert index.is_arguments_for_substr_correct(string, end + 1, 0) == False
    assert index.is_arguments_for_substr_correct(string, end, 5) == False
    assert index.is_arguments_for_substr_correct(string, end, 1) == True
    assert index.is_arguments_for_substr_correct(string, 3, 3) == True
