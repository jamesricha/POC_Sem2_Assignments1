import tkinter as tk 

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        lives = 3
        self.width = 600
        self.height = 400
        self.bg = "#AAAAFF"
        self.Canvas = tk.Canvas(self, bg=self.bg, width = self.width, height = self.height)
        self.Canvas.pack()
        self.pack()

class GameObject(object):
    def __init__(self, Canvas, item):
        self.Canvas = Canvas
        self.item = item

    def get_position(self):
      return self.Canvas.coords(self.item)

    def move(self, x, y):
      self.Canvas.move(self.item, x, y)

    def delete(self):
      self.Canvas.delete(self.item)

if __name__ == '__main__':
    root = tk.Tk()
    frame = tk.Frame(root)
    root.title("BREAKOUT")
    game = Game(root)

    item = game.Canvas.create_rectangle(10, 10, 100, 80, fill="green")
    game_object = GameObject(game.Canvas, item)
    game_object.move(50, 50)
    game_object.delete()

    root.mainloop()