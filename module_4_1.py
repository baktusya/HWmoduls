from fake_math import divide as faked
from true_math import divide as trued

result1 = faked(69, 3)
result2 = faked(5, 0)
result3 = trued(49, 7)
result4 = trued(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)