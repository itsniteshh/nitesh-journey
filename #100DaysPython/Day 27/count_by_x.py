def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    count = 1
    num = []
    for numbers in range(n):
        new = x * count
        num.append(new)
        count += 1
        
    return num