import tkinter


def start(boodschap):
    root = tkinter.Tk()

    main_frame = tkinter.Frame(root)
    tkinter.Label(main_frame, text="Hello World").pack()
    tkinter.Label(main_frame, text=boodschap).pack()

    main_frame.pack()
    root.mainloop()


if __name__ == "__main__":
    start()
