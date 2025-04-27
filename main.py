import tkinter as tk
from PIL import ImageTk, Image

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("Пiсюн клiк")
        self.root.geometry("300x400")
        self.pisun_int = 0

        self.image = Image.open("14.png")
        self.image = self.image.resize((200, 200), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(self.image)

        self.label = tk.Label(root, text=f"Пiсюнчиков натапано: {self.pisun_int}", bg="LightSteelBlue")
        self.label.pack(pady=20)
        self.image_label = tk.Label(root, image=self.photo, bg="LightSteelBlue", cursor="hand2")
        self.image_label.pack(pady=10)
        self.image_label.bind("<Button-1>", lambda event: self.add_clicks())

    def add_clicks(self):
        self.pisun_int += 1
        self.label.config(text=f"Пiсюнчиков натапано: {self.pisun_int}")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="LightSteelBlue")
    game = Game(root)
    root.mainloop()