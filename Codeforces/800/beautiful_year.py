def function(year):
    while True:
        year+=1
        if len(set(str(year))) == len(str(year)):
            break
    return year

def test_example1():
    result = function(1987)
    assert result == 2013

def test_example2():
    result = function(2013)
    assert result == 2014