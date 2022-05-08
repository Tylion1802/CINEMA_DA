from this import d, s
from tkinter import *
import webbrowser
import moviepy.video as mp

def btn_clicked():
    print("Button Clicked")
def phimle():
    window.geometry("1063x804")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 804,
        width = 1063,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
        412.5, 80.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        428.0, 149.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 181.0, y = 131,
        width = 494.0,
        height = 34)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 690, y = 131,
        width = 75,
        height = 36)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimchieurap,
        relief = "flat")

    b1.place(
        x = 526, y = 86,
        width = 113,
        height = 17)

    img2 = PhotoImage(file = f"img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimbo,
        relief = "flat")

    b2.place(
        x = 367, y = 86,
        width = 67,
        height = 17)

    img3 = PhotoImage(file = f"img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimle,
        relief = "flat")

    b3.place(
        x = 226, y = 85,
        width = 58,
        height = 17)

    img4 = PhotoImage(file = f"img4.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b4.place(
        x = 288, y = 493,
        width = 210,
        height = 280)

    img5 = PhotoImage(file = f"img5.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b5.place(
        x = 41, y = 496,
        width = 209,
        height = 273)

    img6 = PhotoImage(file = f"img6.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = alive,
        relief = "flat")

    b6.place(
        x = 828, y = 185,
        width = 207,
        height = 277)

    img7 = PhotoImage(file = f"img7.png")
    b7 = Button(
        image = img7,
        borderwidth = 0,
        highlightthickness = 0,
        command = longchim,
        relief = "flat")

    b7.place(
        x = 569, y = 185,
        width = 207,
        height = 278)

    img8 = PhotoImage(file = f"img8.png")
    b8 = Button(
        image = img8,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b8.place(
        x = 288, y = 184,
        width = 210,
        height = 279)

    img9 = PhotoImage(file = f"img9.png")
    b9 = Button(
        image = img9,
        borderwidth = 0,
        highlightthickness = 0,
        command = vungdat,
        relief = "flat")

    b9.place(
        x = 41, y = 184,
        width = 210,
        height = 280)

    window.resizable(False, False)
    window.mainloop()


    window.geometry("1063x804")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 804,
        width = 1063,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
        412.5, 80.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        428.0, 149.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 181.0, y = 131,
        width = 494.0,
        height = 34)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 690, y = 131,
        width = 75,
        height = 36)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b1.place(
        x = 526, y = 86,
        width = 113,
        height = 17)

    img2 = PhotoImage(file = f"img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b2.place(
        x = 367, y = 86,
        width = 67,
        height = 17)

    img3 = PhotoImage(file = f"img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b3.place(
        x = 226, y = 85,
        width = 58,
        height = 17)

    img4 = PhotoImage(file = f"img4.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b4.place(
        x = 568, y = 185,
        width = 208,
        height = 278)

    img5 = PhotoImage(file = f"img5.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b5.place(
        x = 305, y = 185,
        width = 209,
        height = 279)

    img6 = PhotoImage(file = f"img6.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b6.place(
        x = 41, y = 184,
        width = 210,
        height = 280)

    window.resizable(False, False)
    window.mainloop()

def phimbo():

    window.geometry("1063x804")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 804,
        width = 1063,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
        412.5, 80.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        428.0, 149.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 181.0, y = 131,
        width = 494.0,
        height = 34)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 690, y = 131,
        width = 75,
        height = 36)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimchieurap,
        relief = "flat")

    b1.place(
        x = 526, y = 86,
        width = 113,
        height = 17)

    img2 = PhotoImage(file = f"img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimbo,
        relief = "flat")

    b2.place(
        x = 367, y = 86,
        width = 67,
        height = 17)

    img3 = PhotoImage(file = f"img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimle,
        relief = "flat")

    b3.place(
        x = 226, y = 85,
        width = 58,
        height = 17)

    img20 = PhotoImage(file = f"img20.png")
    b4 = Button(
        image = img20,
        borderwidth = 0,
        highlightthickness = 0,
        command = danhsach,
        relief = "flat")

    b4.place(
        x = 568, y = 185,
        width = 208,
        height = 278)

    img21 = PhotoImage(file = f"img21.png")
    b5 = Button(
        image = img21,
        borderwidth = 0,
        highlightthickness = 0,
        command = walkingdead,
        relief = "flat")

    b5.place(
        x = 305, y = 185,
        width = 209,
        height = 279)

    img22 = PhotoImage(file = f"img22.png")
    b6 = Button(
        image = img22,
        borderwidth = 0,
        highlightthickness = 0,
        command = nhatky,
        relief = "flat")

    b6.place(
        x = 41, y = 184,
        width = 210,
        height = 280)

    window.resizable(False, False)
    window.mainloop()

def phimchieurap():
    window.geometry("1063x804")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 804,
        width = 1063,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"background.png")
    background = canvas.create_image(
        412.5, 80.0,
        image=background_img)

    entry0_img = PhotoImage(file = f"img_textBox0.png")
    entry0_bg = canvas.create_image(
        428.0, 149.0,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 181.0, y = 131,
        width = 494.0,
        height = 34)

    img0 = PhotoImage(file = f"img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 690, y = 131,
        width = 75,
        height = 36)

    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimchieurap,
        relief = "flat")

    b1.place(
        x = 526, y = 86,
        width = 113,
        height = 17)

    img2 = PhotoImage(file = f"img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimbo,
        relief = "flat")

    b2.place(
        x = 367, y = 86,
        width = 67,
        height = 17)

    img3 = PhotoImage(file = f"img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimle,
        relief = "flat")

    b3.place(
        x = 226, y = 85,
        width = 58,
        height = 17)

    img23 = PhotoImage(file = f"img23.png")
    b4 = Button(
        image = img23,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b4.place(
        x = 568, y = 183,
        width = 208,
        height = 280)

    img24 = PhotoImage(file = f"img24.png")
    b5 = Button(
        image = img24,
        borderwidth = 0,
        highlightthickness = 0,
        command = venom,
        relief = "flat")

    b5.place(
        x = 305, y = 183,
        width = 209,
        height = 281)

    img25 = PhotoImage(file = f"img25.png")
    b6 = Button(
        image = img25,
        borderwidth = 0,
        highlightthickness = 0,
        command = kysinhtrung,
        relief = "flat")

    b6.place(
        x = 41, y = 183,
        width = 210,
        height = 281)

    window.resizable(False, False)
    window.mainloop()

def kysinhtrung():
    window.geometry("899x686")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 686,
        width = 899,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    kysinhtrung_img = PhotoImage(file = f"kysinhtrung.png")
    background = canvas.create_image(
        449.5, 343.0,
        image=kysinhtrung_img)

    xemphim = PhotoImage(file = f"xemphim.png")
    b0 = Button(
        image = xemphim,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 530, y = 297,
        width = 139,
        height = 46)

    trolai = PhotoImage(file = f"trolai.png")
    b1 = Button(
        image = trolai,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimchieurap,
        relief = "flat")

    b1.place(
        x = 68, y = 23,
        width = 84,
        height = 33)

    window.resizable(False, False)
    window.mainloop()

def walkingdead():
    window.geometry("899x686")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 686,
        width = 899,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    dead_img = PhotoImage(file = f"dead.png")
    background = canvas.create_image(
        449.5, 343.0,
        image=dead_img)

    trailer = PhotoImage(file = f"trailer.png")
    b0 = Button(
        image = trailer,
        borderwidth = 0,
        highlightthickness = 0,
        command = webbrowser.open_new_tab('https://www.youtube.com/watch?v=qwOWJ8pPgk8&t=9s'),
    
        relief = "flat")

    b0.place(
        x = 530, y = 297,
        width = 139,
        height = 46)

    trolai = PhotoImage(file = f"trolai.png")
    b1 = Button(
        image = trolai,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimbo,
        relief = "flat")

    b1.place(
        x = 68, y = 23,
        width = 84,
        height = 33)

    window.resizable(False, False)
    window.mainloop()

def nhatky():
    window.geometry("899x686")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 686,
        width = 899,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    nhatky_img = PhotoImage(file = f"nhatky.png")
    background = canvas.create_image(
        449.5, 343.0,
        image=nhatky_img)

    trailer = PhotoImage(file = f"trailer.png")
    b0 = Button(
        image = trailer,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 530, y = 297,
        width = 139,
        height = 46)

    trolai = PhotoImage(file = f"trolai.png")
    b1 = Button(
        image = trolai,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimbo,
        relief = "flat")

    b1.place(
        x = 68, y = 23,
        width = 84,
        height = 33)

    window.resizable(False, False)
    window.mainloop()

def vungdat():
    window.geometry("899x686")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 686,
        width = 899,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    vungdat_img = PhotoImage(file = f"vungdat.png")
    background = canvas.create_image(
        449.5, 343.0,
        image=vungdat_img)

    trailer = PhotoImage(file = f"trailer.png")
    b0 = Button(
        image = trailer,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 530, y = 297,
        width = 139,
        height = 46)

    trolai = PhotoImage(file = f"trolai.png")
    b1 = Button(
        image = trolai,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimle,
        relief = "flat")

    b1.place(
        x = 68, y = 23,
        width = 84,
        height = 33)

    window.resizable(False, False)
    window.mainloop()

def alive():
    window.geometry("899x686")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 686,
        width = 899,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    alive_img = PhotoImage(file = f"alive.png")
    background = canvas.create_image(
        449.5, 343.0,
        image=alive_img)

    trailer = PhotoImage(file = f"trailer.png")
    b0 = Button(
        image = trailer,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 530, y = 297,
        width = 139,
        height = 46)

    trolai = PhotoImage(file = f"trolai.png")
    b1 = Button(
        image = trolai,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimle,
        relief = "flat")

    b1.place(
        x = 68, y = 23,
        width = 84,
        height = 33)

    window.resizable(False, False)
    window.mainloop()

def longchim():
    window.geometry("899x686")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 686,
        width = 899,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    longchim_img = PhotoImage(file = f"longchim.png")
    background = canvas.create_image(
        449.5, 343.0,
        image=longchim_img)

    trailer = PhotoImage(file = f"trailer.png")
    b0 = Button(
        image = trailer,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 530, y = 297,
        width = 139,
        height = 46)

    trolai = PhotoImage(file = f"trolai.png")
    b1 = Button(
        image = trolai,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimle,
        relief = "flat")

    b1.place(
        x = 68, y = 23,
        width = 84,
        height = 33)

    window.resizable(False, False)
    window.mainloop()

def danhsach():
    window.geometry("899x686")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 686,
        width = 899,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    danhsach_img = PhotoImage(file = f"danhsach.png")
    background = canvas.create_image(
        449.5, 343.0,
        image=danhsach_img)

    trailer = PhotoImage(file = f"trailer.png")
    b0 = Button(
        image = trailer,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 530, y = 297,
        width = 139,
        height = 46)

    trolai = PhotoImage(file = f"trolai.png")
    b1 = Button(
        image = trolai,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimbo,
        relief = "flat")

    b1.place(
        x = 68, y = 23,
        width = 84,
        height = 33)

    window.resizable(False, False)
    window.mainloop()

def venom():
    window.geometry("899x686")
    window.configure(bg = "#091b27")
    canvas = Canvas(
        window,
        bg = "#091b27",
        height = 686,
        width = 899,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    venom2_img = PhotoImage(file = f"venom2.png")
    background = canvas.create_image(
        449.5, 343.0,
        image=venom2_img)

    trailer = PhotoImage(file = f"trailer.png")
    b0 = Button(
        image = trailer,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    b0.place(
        x = 530, y = 297,
        width = 139,
        height = 46)

    trolai = PhotoImage(file = f"trolai.png")
    b1 = Button(
        image = trolai,
        borderwidth = 0,
        highlightthickness = 0,
        command = phimchieurap,
        relief = "flat")

    b1.place(
        x = 68, y = 23,
        width = 84,
        height = 33)

    window.resizable(False, False)
    window.mainloop()


window = Tk()

window.geometry("1063x804")
window.configure(bg = "#091b27")
canvas = Canvas(
    window,
    bg = "#091b27",
    height = 804,
    width = 1063,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    428.0, 149.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 181.0, y = 131,
    width = 494.0,
    height = 34)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 690, y = 131,
    width = 75,
    height = 36)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    412.5, 80.0,
    image=background_img)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = phimchieurap,
    relief = "flat")

b1.place(
    x = 526, y = 86,
    width = 113,
    height = 17)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = phimbo,
    relief = "flat")

b2.place(
    x = 367, y = 86,
    width = 67,
    height = 17)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = phimle,
    relief = "flat")

b3.place(
    x = 226, y = 85,
    width = 58,
    height = 17)

window.resizable(False, False)
window.mainloop()



