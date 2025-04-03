# Description: This script creates a Tkinter canvas with a grid of blue cells.
# The user can click and drag to erase the blue cells using a red eraser rectangle.
# The eraser rectangle is larger than the cells, allowing for easy erasing of multiple cells at once.
# The script also includes a message to guide the user on how to use the eraser.
import tkinter as tk
CELL_SIZE = 20
ROWS = 20
COLS = 20
ERASER_SIZE = 40

class CanvasApp:

    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="white")
        self.canvas.pack()

        self.is_erasing = False
        self.eraser_rect = None

        self.draw_grid()
        self.setup_events()

        # Message to guide user
        print("Click and drag to erase the blue cells!")

    def draw_grid(self):
        # Draw grid of blue cells
        self.cells = []
        for row in range(ROWS):
            row_cells = []
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                cell = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                row_cells.append(cell)
            self.cells.append(row_cells)

    def setup_events(self):
        # Bind mouse events for erasing
        self.canvas.bind("<ButtonPress-1>", self.start_erasing)   # Start erasing on mouse click
        self.canvas.bind("<B1-Motion>", self.erase)               # Erase while mouse is moving
        self.canvas.bind("<ButtonRelease-1>", self.stop_erasing)  # Stop erasing on mouse release

    def start_erasing(self, event):
        self.is_erasing = True
        self.update_eraser(event)

    def erase(self, event):
        if self.is_erasing:
            self.update_eraser(event)

    def stop_erasing(self, event):
        self.is_erasing = False
        if self.eraser_rect:
            self.canvas.delete(self.eraser_rect)

    def update_eraser(self, event):
        x = event.x - ERASER_SIZE // 2
        y = event.y - ERASER_SIZE // 2

        # Remove previous eraser rectangle
        if self.eraser_rect:
            self.canvas.delete(self.eraser_rect)

        # Draw the eraser rectangle
        self.eraser_rect = self.canvas.create_rectangle(
            x, y, x + ERASER_SIZE, y + ERASER_SIZE,
            outline="red", width=2
        )

        # Call the erase function to erase cells
        self.erase_cells(x, y)

    def erase_cells(self, eraser_x, eraser_y):
        for row in range(ROWS):
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE

                # Check if the eraser overlaps with the cell
                if (
                    x1 < eraser_x + ERASER_SIZE and
                    x2 > eraser_x and
                    y1 < eraser_y + ERASER_SIZE and
                    y2 > eraser_y
                ):
                    self.canvas.itemconfig(self.cells[row][col], fill="white")

def main():
    root = tk.Tk()
    root.title("Canvas Eraser")  # Set the window title
    app = CanvasApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
