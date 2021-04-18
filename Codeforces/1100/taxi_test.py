def function(n, num_list):
    num_list = list(map(int, num_list.split()))

    count1, count2, count3, count4 = 0,0,0,0

    for num in num_list:
        if num == 4: count4 +=1
        elif num == 3: count3 += 1
        elif num == 2: count2 += 1
        else: count1 += 1

    result = count4

    result += count2//2
    count2 = count2%2

    if count1 <= count3:
        result += count1
        result += count2
        result += count3 - count1
    else:
        result += count3
        count1 -= count3
        result += count1 // 4
        count1 %= 4

        res = count1 + count2 * 2
        if res > 0:
            result += 1 if res <= 4 else 2

    return result

def test_example1():
    result = function(8, '2 3 4 4 2 1 3 1')
    assert result == 5

def test_example2():
    result = function(5, '1 2 4 3 3')
    assert result == 4

def test_example3():
    result = function(16, '4 3 3 3 2 2 2 1 1 1 1 1 1 1 1 1')
    assert result == 7

def test_example4():
    result = function(0, '')
    assert result == 0

def test_example5():
    result = function(1, '2')
    assert result == 1