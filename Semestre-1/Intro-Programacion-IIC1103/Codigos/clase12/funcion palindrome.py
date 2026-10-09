def palindrome(s):
    for i in range(len(s)//2):
        if s[i]!=s[-1*i-1]:
            return False
    return True

def palindrome2(s):
    if s == s[::-1]:
        return True
    else:
        return False
def palindrome3(s):
    return s == s[::-1]


for i in range(10):
    palabra = input()
    print(palindrome(palabra))

