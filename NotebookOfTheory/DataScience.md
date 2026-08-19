> [!IMPORTANT]
> This part dedicated to Data Science this is the part 0.4 in my plan.

*I want write fucntions from a few libraries in python.*

# Collections:
 - Counter:
   - Example:
   ```Python
   from collections import Couter

   counts = Counter(['apple', 'banana', 'apple', 'banana'])
   print(counts) # Output: Counter({'apple': 2, 'banana': 2})
   ```
 - Deque:
   - Example:
   ```Python
   from collections import deque

   queue = deque(['task1', 'task2'])
   queue.append('task3') # Add to the right end
   queue.appendleft('task0') # Add to the left end
   queue.popleft() # Remove from the left end

   print(queue) # Output: deque(['task1', 'task2', 'task3'])
   ```
 - NamedTuple
   - Example:
   ```Python
   from collections import namedtuple

   Point = namedtuple('Point', ['x', 'y'])
   p = Point(10,20)

   print(p.x, p.y) # Output: 10 20
   ```

## Numpy:
 - Vectorize: It is a function which can use list, doesn't use loop.
 ```Python
 import numpy as np

 def myfunc(list):
    "Return list inside which objects, replace to "GOOD" and "BAD" depending on they value."
    if list > 10 and list < 100:
        return "GOOD"
    else:
        return "BAD"
 sort = np.vectorize(myfunc)
 vector = np.array([1,20,40,55,67,302,999])
 print(sort(vector)) # Output: ['BAD', 'GOOD', 'GOOD', 'GOOD', 'GOOD', 'BAD', 'BAD']
 ```

## Pandas
    - I'll finish writing this part later.
