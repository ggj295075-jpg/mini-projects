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
 - Vectorize:
 ```Python
 import numpy as np

 def myfunc(list):

