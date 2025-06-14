no_of_prize = int(input())
pos = list(map(int, input().split()))
pos.sort()

mid = (10**6) / 2


if mid in pos:
    time = int(mid - 1)

else: 
    dist_from_a, dist_from_b = 0, 0
    for i in pos:
        if i < mid:
            dist_from_a = max(dist_from_a, abs(i - 1))

        if i > mid:
            dist_from_b = max(dist_from_b, abs(i - (10**6)))

    if dist_from_a > dist_from_b:
        time = dist_from_a

    else:
        time = dist_from_b

print(int(time))

    





# for i in pos:
#     i = int(i)

#     dist_from_a = abs(i - 1)
#     dist_from_b = abs(i - 10**6)

#     if dist_from_a >= dist_from_b:
#         time += abs(i - 10**6)
#     else:
#         time += abs(i - 1)

# print(int(time))

# pos = np.array(pos).astype("int")

# dist_from_a = abs(pos - 1)
# dist_from_b = abs(pos - 10**6)

# t_f_array = dist_from_a >= dist_from_b

# time = 0
# for i in t_f_array:
#     if i:
#         time += abs(pos - 10**6)
#     else:
#         time += abs(pos - 1)



