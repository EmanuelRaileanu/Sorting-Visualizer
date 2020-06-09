import time

def bubbleSort(arr, drawData, timeTick):
	ok = True
	while ok:
		ok = False
		for i in range(len(arr) - 1):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				drawData(arr, ["limegreen" if x == i or x == i + 1 else "deepskyblue" for x in range(len(arr))])
				time.sleep(timeTick)
				ok = True