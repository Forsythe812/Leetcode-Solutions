def defangIPaddr(address):
    fixed = address.replace('.','[.]')
    return fixed
print(defangIPaddr("1.1.1.1"))