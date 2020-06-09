import time

def quickSort(arr, l, r, drawData, timeTick):
	if l < r:
 		i = l
 		pivot = arr[r]
 		for j in range(l, r):
 			if arr[j] <= pivot:
 				if arr[i] != arr[j]:
 					arr[i], arr[j] = arr[j], arr[i]
 					drawData(arr, ["red" if x == r  else "limegreen" if x == i or x == j else "deepskyblue" for x in range(len(arr))])
 					time.sleep(timeTick)
 				i = i + 1
 		arr[i], arr[r] = arr[r], arr[i]
 		drawData(arr, ["red" if x == r  else "limegreen" if x == i else "deepskyblue" for x in range(len(arr))])
 		time.sleep(timeTick)
 		quickSort(arr, l, i - 1, drawData, timeTick)
 		quickSort(arr, i + 1, r, drawData, timeTick)
