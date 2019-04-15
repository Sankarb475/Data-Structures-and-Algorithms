Priority Queues
=============================================================================================================================
One important variation of a queue is called a priority queue. A priority queue acts like a queue in that you dequeue an item 
by removing it from the front. However, in a priority queue the logical order of items inside a queue is determined by their 
priority. The highest priority items are at the front of the queue and the lowest priority items are at the back. Thus when 
you enqueue an item on a priority queue, the new item may move all the way to the front. We will see that the priority queue 
is a useful data structure for some of the graph algorithms we will study in the next chapter.

You can probably think of a couple of easy ways to implement a priority queue using sorting functions and lists. However, 
inserting into a list is O(n) and sorting a list is O(nlogn). We can do better. The classic way to implement a priority queue 
is using a data structure called a binary heap. A binary heap will allow us both enqueue and dequeue items in O(logn).

Heaps are binary trees for which every parent node has a value less than or equal to any of its children.

You can use the following package to use the rich features of priority queues (heap queue) ::

>>> import heapq

To create a heap, use a list initialized to [], or you can transform a populated list into a heap via function heapify().


import heapq

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]

print(heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0]))

output => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


please go through the following link for detailed description ::
https://docs.python.org/3/library/heapq.html

