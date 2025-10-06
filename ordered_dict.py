from collections import OrderedDict

nums = [1,2,3,4,5,6]
od = OrderedDict.fromkeys(nums)
d = dict.fromkeys(nums)
print(od)
print(d)