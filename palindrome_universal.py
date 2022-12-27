def is_palindrome(n):
    nstr = str(n).lower()    
    rev_string = nstr[::-1]    
    if rev_string == nstr:
        return True
    else:
        return False

print(is_palindrome('Anna'))    #True
print(is_palindrome('walter'))  #False
print(is_palindrome(12321))     #True
print(is_palindrome(123456))    #False


#2nd method
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]