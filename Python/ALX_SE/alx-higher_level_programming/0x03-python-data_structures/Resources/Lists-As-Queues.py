# Using Python Lists as queues
# Lists are mutable, and their elements are usually homogeneous and are accessed by iterating over the list.
from collections import deque

dan = deque(["Eric", "John", "Micheal"])
print(dan)
dan.append("Daniel")        # Daniel arrives
dan.append("Jon Bellion")   # Jon Bellion arrives

dan.popleft()
print(dan.popleft())        # The first to arrive now leaves

dan.popleft()
print(dan.popleft())        # The second to arrive now leaves


print(dan)

