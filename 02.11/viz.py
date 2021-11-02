import tkinter as tk

window = tk.Tk()

label = tk.Label(
  text = "Sveiki! Sveiki! Sveiki! Sveiki!",
  foreground = "red",
  background = "#34A2FE"
  )

label1 = tk.Label(
  text = "Čau!",
  fg = "red",
  bg = "#34A2AE",
  width = 10,
  height = 10
  )

label.pack()
label1.pack()

window.mainloop()