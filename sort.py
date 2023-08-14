import tkinter as tk
from tkinter import Canvas
from random import randint
import time

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Algorithms Visualizer")
        
        self.array = [randint(10, 450) for _ in range(20)]
        
        self.canvas = Canvas(self.root, width=600, height=500, bg="white")
        self.canvas.pack(pady=20)

        self.draw_array(self.array)

        # Buttons to trigger sorting algorithms
        bubble_sort_button = tk.Button(self.root, text="Bubble Sort", command=self.bubble_sort)
        bubble_sort_button.pack(side=tk.LEFT, padx=10)

        selection_sort_button = tk.Button(self.root, text="Selection Sort", command=self.selection_sort)
        selection_sort_button.pack(side=tk.LEFT, padx=10)

        insertion_sort_button = tk.Button(self.root, text="Insertion Sort", command=self.insertion_sort)
        insertion_sort_button.pack(side=tk.LEFT, padx=10)

        regenerate_button = tk.Button(self.root, text="Regenerate Array", command=self.regenerate_array)
        regenerate_button.pack(side=tk.LEFT, padx=10)


    def draw_array(self, array, color=['blue'] * 20):
        self.canvas.delete("all")
        c_width = 600
        c_height = 500
        x_width = c_width / (len(array) + 1)
        offset = 30
        spacing = 10
        normalized_array = [i / max(array) * (c_height - offset) for i in array]

        for i, height in enumerate(normalized_array):
            # top left
            x0 = i * x_width + offset + spacing
            y0 = c_height - height
            # bottom right
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color[i])
            self.canvas.create_text(x0 + x_width / 2, y0, anchor=tk.SW, text=str(array[i]))

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    self.draw_array(self.array)
                    self.canvas.update()
                    time.sleep(0.2)
        
    def selection_sort(self):
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.draw_array(self.array)
            self.canvas.update()
            time.sleep(0.2)
        
    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i-1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            self.draw_array(self.array)
            self.canvas.update()
            time.sleep(0.2)

    def regenerate_array(self):
   
        self.array = [randint(10, 450) for _ in range(20)]
        self.draw_array(self.array)
       

# Create the main window
root = tk.Tk()
visualizer = SortingVisualizer(root)
root.mainloop()
