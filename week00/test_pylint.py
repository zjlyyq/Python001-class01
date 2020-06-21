import heapq

heap = []

for i in range(10, 0, -1):
    heapq.heappush(heap, i)

print(heap)


