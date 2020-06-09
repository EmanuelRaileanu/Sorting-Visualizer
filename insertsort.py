import time

def insertSort(arr, drawData, timeTick):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j + 1] = arr[j]
			drawData(arr, ["limegreen" if x == j or x == j + 1 else "deepskyblue" for x in range(len(arr))])
			time.sleep(timeTick)
			j -= 1
		arr[j + 1] = key
