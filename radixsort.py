import time

def countingSort(arr, exp, drawData, timeTick):
	output = [0] * (len(arr))
	count = [0] * (10)
	for i in range(len(arr)):
		index = arr[i] // exp
		count[index % 10] += 1
	for i in range(1, 10):
		count[i] += count[i - 1]

	i = len(arr) - 1
	while i >= 0:
		index = arr[i] // exp
		output[count[index % 10] - 1] = arr[i]
		count[index % 10] -= 1
		i -= 1

	i = 0
	for i in range(len(arr)):
		arr[i] = output[i]
		drawData(arr, ["limegreen" if x == i else "deepskyblue" for x in range(len(arr))])
		time.sleep(timeTick)

def radixSort(arr, drawData, timeTick):
	max_  = max(arr)
	exp = 1
	while max_ / exp > 1:
		countingSort(arr, exp, drawData, timeTick)
		exp *= 10