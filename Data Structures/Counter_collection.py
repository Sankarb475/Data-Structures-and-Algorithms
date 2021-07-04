Python has a Counter collection - which stores the count of each element in the collection, in a key-value pair storage.

-- it does not guarantee an order of element stored.

-- We may think of counter as an unordered collection of items where items are stored as dictionary keys and their count as dictionary value.
-- Its under collections module in python


from collections import Counter
nums = [1,3,5,3,9]

freq=Counter(nums)
print(freq)
print(type(freq))

Counter({3: 2, 1: 1, 5: 1, 9: 1})
<class 'collections.Counter'>


-- you can check the duplicate values using this
