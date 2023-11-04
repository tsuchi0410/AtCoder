import heapq
K = int(input())

h = [1, 2, 3, 4, 5, 6, 7, 8, 9]
heapq.heapify(h)

cnt = 1
while True:
    h_min = heapq.heappop(h)
    if cnt == K:
        print(h_min)
        exit()
    else:
        cnt += 1
        s = str(h_min)
        if s[-1] == "0":
            heapq.heappush(h, 10 * h_min)
            heapq.heappush(h, 10 * h_min + 1)
        elif s[-1] == "9":
            heapq.heappush(h, 10 * h_min + 8)
            heapq.heappush(h, 10 * h_min + 9)
        else:
            heapq.heappush(h, 10 * h_min + (int(s[-1]) - 1))
            heapq.heappush(h, 10 * h_min + int(s[-1]))
            heapq.heappush(h, 10 * h_min + (int(s[-1]) + 1))
