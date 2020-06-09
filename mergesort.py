import time

def mergeSort(data, left, right, drawData, timeTick):
	if left < right:
		middle = (left + right) // 2
		mergeSort(data, left, middle, drawData, timeTick)
		mergeSort(data, middle + 1, right, drawData, timeTick)

		drawData(data, getColorArray(len(data), left, middle, right))
		time.sleep(timeTick)

		left_arr = data[left: middle + 1]
		right_arr = data[middle + 1: right + 1]

		left_index = right_index = 0
		for data_index in range(left, right + 1):
			if left_index < len(left_arr) and right_index < len(right_arr):
				if left_arr[left_index] <= right_arr[right_index]:
					data[data_index] = left_arr[left_index]
					left_index += 1
				else:
					data[data_index] = right_arr[right_index]
					right_index += 1
			elif left_index < len(left_arr):
				data[data_index] = left_arr[left_index]
				left_index += 1
			else:
				data[data_index] = right_arr[right_index]
				right_index += 1
		drawData(data, ["limegreen" if x >= left and x <= right else "deepskyblue" for x in range(len(data))])
		time.sleep(timeTick)

def getColorArray(lenght, left, middle, right):
	colorArray = []

	for i in range(lenght):
		if i >=left and i <= right:
			if i >=  left and i <= middle:
				colorArray.append("yellow")
			else:
				colorArray.append("orange")
		else:
			colorArray.append("deepskyblue")

	return colorArray
