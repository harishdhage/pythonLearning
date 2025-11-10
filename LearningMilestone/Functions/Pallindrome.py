
def check_pallindrome(st):
    st = st.lower().replace(" ","")
    return st == st[::-1]

print(check_pallindrome("Gadag"))
print(check_pallindrome("A man a plan a canal Panama"))
print(check_pallindrome("A man a plan a canal Panamaa"))