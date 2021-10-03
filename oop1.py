n = 5

# Create 2D array
main_arr = []
for i in range(0, n):
    main_arr.append([])
    

counter = 1
for i in range(1, n + 1):
    temp_arr = [0 for _ in range(i)]
    if i%2 != 0:
        for j in range(0, i):
            temp_arr[j] = counter
            counter += 1
    if i%2 == 0:
        for j in range(i-1, -1, -1):
            temp_arr[j] = counter
            counter += 1

    main_arr[i-1] = temp_arr

for r in range(len(main_arr)):
    print(main_arr[r])