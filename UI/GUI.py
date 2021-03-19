import tkinter as tk
from UI.Main import MainPage


# inherit tkinter functionality


class UI(tk.Tk):

    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.bind("<Escape>", lambda e: self.quit())
        self.title("BLI")
        self.geometry("300x200")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # configure the rows and columns (0 is setting te minimum size, weight is the priority)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, SettingsPage):

            frame = F(container, self)
            self.frames[F] = frame

            # sticky is the alignment and stretch (nsew is north, south, east, west)

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

        # animation = self.frames[GraphFrame].start_animation()
        # animation = self.frames[MainPage].gf.start_animation()

        self.mainloop()

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="start page", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Start", command=lambda : self.start_main_page(controller))
        button1.pack()

    def start_main_page(self, controller):
        controller.destroy()
        MainPage()






class SettingsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="start page", font="LARGE_FONT")
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Start", command=lambda: controller.show_frame)
        button1.pack()










if __name__ == "__main__":
    app = UI()
