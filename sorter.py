from tkinter import *
from tkinter import ttk
import random
import time
from quicksort import quickSort
from mergesort import mergeSort
from insertsort import insertSort
from bubblesort import bubbleSort
from radixsort import radixSort
from selectsort import selectSort

root = Tk()
root.title("Sorting Algorithm Visualizer")
root.maxsize(1200, 900)
root.config(bg = "black")

#variables
selected_algorithm = StringVar()
data = []

def drawData(data, colorArray):
	canvas.delete("all")
	canvas_height = 580
	canvas_width = 1200
	x_width = canvas_width / (len(data) + 1)
	offset = (canvas_width - (x_width * sizeEntry.get())) // 2 - 2
	spacing = 0
	normalizedData = [i / max(data) for i in data]
	for i, height in enumerate(normalizedData):
		#top left
		x0 = i * x_width + offset + spacing
		y0 = canvas_height - height * 540
		#bottom right
		x1 = (i + 1) * x_width + offset
		y1 = canvas_height
		canvas.create_rectangle(x0, y0, x1, y1, fill = colorArray[i])
		if sizeEntry.get() <= 100:
			canvas.create_text(x0 + 2, y0, anchor = SW, font=("Arial", 18 if sizeEntry.get() <= 30 else int(x_width - 4) // 2), text = str(data[i]))
	root.update_idletasks()

def Generate():
	global data
	minVal = int(minEntry.get())
	maxVal = int(maxEntry.get())
	size = int(sizeEntry.get())

	if minVal > maxVal:
		minVal, maxVal = maxVal, minVal

	data = []
	for _ in range(size):
		data.append(random.randrange(minVal, maxVal + 1))
	buff = data
	drawData(data, ["deepskyblue" for x in range(len(data))])

def StartAlgorithm():
	global data
	if algMenu.get() == "Quick sort":
		quickSort(data, 0, len(data) - 1, drawData, speedScale.get() / 1000)
	elif algMenu.get() == "Merge sort":
		mergeSort(data, 0, len(data) - 1, drawData, speedScale.get() / 1000)
	elif algMenu.get() == "Selection sort":
		selectSort(data, drawData, speedScale.get() / 1000)
	elif algMenu.get() == "Radix sort":
		radixSort(data, drawData, speedScale.get() / 1000)
	elif algMenu.get() == "Insertion sort":
		insertSort(data, drawData, speedScale.get() / 1000)
	elif algMenu.get() == "Bubble sort":
		bubbleSort(data, drawData, speedScale.get() / 1000)

	drawData(data, ["limegreen" for _ in range(len(data))])

def StopAlgorithm():
	x = 1

#frame
UI_frame = Frame(root, width = 1200, height = 300, bg = "grey")
UI_frame.grid(row = 0, column = 0, padx = 5, pady = 5)

canvas = Canvas(root, width = 1200, height = 580)
canvas.grid(row = 1, column = 0, padx = 5, pady = 5)

#User Interface Area
#Row 0
Label(UI_frame, text = "Algorithm: ", bg = "grey").grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)
algMenu = ttk.Combobox(UI_frame, textvariable =  selected_algorithm, values = ["Quick sort", "Merge sort", "Selection sort", "Radix sort", "Insertion sort", "Bubble sort"])
algMenu.grid(row = 0, column = 0, columnspan = 2, padx = 90, pady =5, sticky = W)
algMenu.current(0)

speedScale = Scale(UI_frame, from_ = 1, to = 2000, length = 500, resolution = 5, orient = HORIZONTAL, label = "Select Speed (ms)")
speedScale.grid(row = 0, column = 1, columnspan = 2, padx = 5, pady = 5, sticky = E)
speedScale.set(100)
Button(UI_frame, text = "Start", command = StartAlgorithm, bg = "limegreen").grid(row = 0, column = 3, padx = 5, pady = 5)
Button(UI_frame, text = "Stop", command = StopAlgorithm, bg = "red").grid(row = 0, column = 4, padx = 5, pady = 5)

#Row 1
sizeEntry = Scale(UI_frame, from_ = 0, to = 400, length = 400, resolution = 1, orient = HORIZONTAL, label = "Array size")
sizeEntry.grid(row = 1, column = 0, padx = 5, pady = 5)
sizeEntry.set(10)

minEntry = Scale(UI_frame, from_ = 0, to = 150, length = 250, resolution = 1, orient = HORIZONTAL, label = "Min value")
minEntry.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

maxEntry = Scale(UI_frame, from_ = 0, to = 200, length = 250, resolution = 1, orient = HORIZONTAL, label = "Max value")
maxEntry.grid(row = 1, column = 2, padx = 5, pady = 5, sticky = E)
maxEntry.set(50)

Button(UI_frame, text = "Generate new array", command = Generate, bg = "white").grid(row = 1, column = 3, columnspan = 2, padx = 5, pady = 5)

root.mainloop()