dct = {'1':1,'22':22,'333':333,'4444':4444}

# Adding an element at the last of the dictionary
dct['py'] = 'python'

# Deleting the first element of the dictionary
first_item = next(iter(dct))
del dct[first_item]

print(dct)
