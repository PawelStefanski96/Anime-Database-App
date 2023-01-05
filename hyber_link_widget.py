from ttkwidgets import LinkLabel
import tkinter as tk

window = tk.Tk()
LinkLabel(window, text="ttkwidgets repository",
          link="https://github.com/RedFantom/ttkwidgets",
          normal_color='royal blue',
          hover_color='blue',
          clicked_color='purple').pack()
window.mainloop()