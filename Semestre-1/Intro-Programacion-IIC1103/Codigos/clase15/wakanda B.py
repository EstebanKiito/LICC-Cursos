def sepuede(m, i):
    if m[i - 1] == '-' and m[i] == '-' and m[i + 1] == '-':
        return True
    else:
        return False

