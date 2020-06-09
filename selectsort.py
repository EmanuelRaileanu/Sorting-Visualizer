import time

def selectSort(arr, drawData, timeTick):
	for i in range(len(arr)):
		min_index = i
		for j in range(i + 1, len(arr)):
			if arr[min_index] > arr[j]:
				min_index = j
				drawData(arr, ["red" if x == min_index else "limegreen" if x == i else "deepskyblue" for x in range(len(arr))])
				time.sleep(timeTick)
		arr[i], arr[min_index] = arr[min_index], arr[i]
		drawData(arr, ["red" if x == min_index else "limegreen" if x == i else "deepskyblue" for x in range(len(arr))])
		time.sleep(timeTick)