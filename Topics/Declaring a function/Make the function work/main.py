def closest_higher_mod_5(x):
    remainder = x % 5
    if remainder >=  x:
        return x
    return remainder