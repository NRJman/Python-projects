from tkinter import *
from graphics import *
import time
import pygame
from pygame import gfxdraw
num = 10
pixel_size = 5


#==================================================Printer==============================================================
def donothing ():
    return 0



def draw_pixel(surface, x, y, color):
    pixel_size = 5
    for x_coord in range(x, x + pixel_size):
        for y_coord in range(y, y + pixel_size):
            gfxdraw.pixel(surface, x_coord, y_coord, color)


def DDA_line(surface, x0, y0, x1, y1, color):
    pixel_size = 5
    x_diff, y_diff = x1 - x0, y1 - y0
    L = max(abs(x1 - x0), abs(y1 - y0))
    dx, dy = x_diff / float(L), y_diff / float(L)

    x, y = x0, y0
    for i in range(L + 1):
        draw_pixel(surface, pixel_size * int(round(x)), pixel_size * int(round(y)), color)
        x += dx
        y += dy


def Bresenham_line(surface, x0, y0, x1, y1, color):
    dy = dx = 1
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    if y0 > y1:
        dy = -1

    x_diff, y_diff = abs(x1 - x0), abs(y1 - y0)

    if x_diff >= y_diff:

        error = 0
        delta_err = y_diff

        y = y0
        for x in range(x0, x1 + 1):
            draw_pixel(surface, pixel_size * x, pixel_size * y, color)
            error += delta_err
            if (2 * error >= x_diff):
                y += dy
                error -= x_diff
    else:
        if x0 > x1:
            dx = -1

        error = 0
        delta_err = x_diff

        x = x0
        for y in range(y0, y1 + 1, dy):
            draw_pixel(surface, pixel_size * x, pixel_size * y, color)
            error += delta_err
            if (2 * error >= y_diff):
                x += dx
                error -= y_diff


def Bresenham_circle(surface, x0, y0, R, color):
    x = 0
    y = R
    error = 1 - R
    while x <= y:
        draw_pixel(surface, pixel_size * (x0 + x), pixel_size * (y0 + y), color)
        draw_pixel(surface, pixel_size * (x0 + x), pixel_size * (y0 - y), color)
        draw_pixel(surface, pixel_size * (x0 - x), pixel_size * (y0 + y), color)
        draw_pixel(surface, pixel_size * (x0 - x), pixel_size * (y0 - y), color)
        draw_pixel(surface, pixel_size * (x0 + y), pixel_size * (y0 + x), color)
        draw_pixel(surface, pixel_size * (x0 + y), pixel_size * (y0 - x), color)
        draw_pixel(surface, pixel_size * (x0 - y), pixel_size * (y0 + x), color)
        draw_pixel(surface, pixel_size * (x0 - y), pixel_size * (y0 - x), color)

        if error > 0:
            y -= 1
            error += 2 * (x - y) + 5
        else:
            error += 2 * x + 3
        x += 1


def Wu_line(surface, x0, y0, x1, y1, color):
    if x0 == x1:
        for y in range(min(y0, y1), max(y0, y1)):
            draw_pixel(surface, pixel_size * x0, pixel_size * y, color)
        return

    if y0 == y1:
        for x in range(min(x0, x1), max(x0, x1)):
            draw_pixel(surface, pixel_size * x, pixel_size * y0, color)
        return

    x = y = 0
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0

    x_diff, y_diff = x1 - x0, y1 - y0

    if (abs(x_diff) >= abs(y_diff)):
        grad = y_diff / float(x_diff)

        draw_pixel(surface, pixel_size * x0, pixel_size * y0, color)
        y = y0 + grad
        for x in range(x0 + 1, x1):
            k = y - int(y)
            draw_pixel(surface, pixel_size * x, pixel_size * int(y), (color[0], int(255 * k), int(255 * k)))
            draw_pixel(surface, pixel_size * x, pixel_size * (int(y) + 1),
                       (color[0], int(255 * (1 - k)), int(255 * (1 - k))))
            y += grad
        draw_pixel(surface, pixel_size * x1, pixel_size * y1, color)
    else:
        if (y0 > y1):
            y0, y1 = y1, y0
            x0, x1 = x1, x0

        grad = x_diff / float(y_diff)

        draw_pixel(surface, pixel_size * x0, pixel_size * y0, color)
        x = x0 + grad
        for y in range(y0 + 1, y1):
            k = x - int(x)
            draw_pixel(surface, pixel_size * int(x), pixel_size * y, (color[0], int(255 * k), int(255 * k)))
            draw_pixel(surface, pixel_size * (int(x) + 1), pixel_size * y,
                       (color[0], int(255 * (1 - k)), int(255 * (1 - k))))
            x += grad
        draw_pixel(surface, pixel_size * x1, pixel_size * y1, color)


def name_draw(surface, color):
    #V
    Bresenham_line(surface, 5, 4, 10, 15, color)
    Bresenham_line(surface, 10, 15, 17, 2, color)
    #A
    Bresenham_line(surface, 20, 4, 15, 15, color)
    Bresenham_line(surface, 20, 4, 25, 15, color)
    Bresenham_line(surface, 20, 3, 15, 15, color)
    Bresenham_line(surface, 18, 10, 22, 10, color)
    #D
    Bresenham_line(surface, 28, 4, 28, 15, color)
    Bresenham_line(surface, 28, 4, 30, 4, color)
    Bresenham_line(surface, 30, 4, 33, 5, color)
    Bresenham_line(surface, 33, 5, 33, 13, color)
    Bresenham_line(surface, 33, 12, 31, 15, color)
    Bresenham_line(surface, 31, 15, 28, 15, color)
    #Y
    Bresenham_line(surface, 36, 4, 40, 10, color)
    Bresenham_line(surface, 40, 10, 45, 2, color)
    Bresenham_line(surface, 40, 10, 40, 15, color)
    #M
    Bresenham_line(surface, 48, 2, 44, 15, color)
    Bresenham_line(surface, 48, 4, 50, 9, color)
    Bresenham_line(surface, 50, 9, 53, 2, color)
    Bresenham_line(surface, 50, 9, 53, 2, color)
    Bresenham_line(surface, 53, 4, 56, 15, color)


#==============================================Bresenham line===========================================================
def BresenhamLine(x1, y1, x2, y2):
    """ Bresenham Line Drawing Algorithm For All Kind Of Slopes Of Line """

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    slope = dy / float(dx)

    x, y = x1, y1

    # creating the window
    win = GraphWin('Brasenham Line', 600, 480)

    # checking the slope if slope > 1
    # then interchange the role of x and y
    if slope > 1:
        dx, dy = dy, dx
        x, y = y, x
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # initialization of the inital disision parameter
    p = 2 * dy - dx

    PutPixle(win, x, y)
    for k in range(2, dx):
        if p > 0:
            y = y + 1 if y < y2 else y - 1
            p = p + 2 * (dy - dx)
        else:
            p = p + 2 * dy

        x = x + 1 if x < x2 else x - 1

        # delay for 0.01 secs
        time.sleep(0.01)
        PutPixle(win, x, y)


def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    pt = Point(x, y)
    pt.draw(win)

def main():
    x1 = int(input("Enter Start X: "))
    y1 = int(input("Enter Start Y: "))
    x2 = int(input("Enter End X: "))
    y2 = int(input("Enter End Y: "))
    BresenhamLine(x1, y1, x2, y2)
#==============================================Bresenham circle=========================================================
def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    pt = Point(x, y)
    pt.draw(win)


def drawCircle(x0, y0, radius):
    win = GraphWin('Brasenham Circle', 600, 480)
    x = 0
    y = radius
    delta = 1 - 2*radius
    error = 0
    while y >= 0:
        time.sleep(0.01)
        PutPixle(win, x0 + x, y0 + y)
        time.sleep(0.01)
        PutPixle(win, x0 + x, y0 - y)
        time.sleep(0.01)
        PutPixle(win, x0 - x, y0 + y)
        time.sleep(0.01)
        PutPixle(win, x0 - x, y0 - y)
        error = 2 * (delta + y) - 1
        if delta < 0 and error <= 0:
            x += 1
            delta += 2 * x + 1
            continue
        error = 2 * (delta - x) - 1
        if delta > 0 and error > 0:
            y -= 1
            delta += 1 - 2 * y
            continue
        x += 1
        delta += 2 * (x - y)
        y -= 1
#=======================================================================================================================
def TurnOnDDA(event):
    window_width = 1024
    window_height = 768

    screen_color = (255, 255, 255)
    draw_color = (255, 0, 0)

    DDA_x0, DDA_y0, DDA_x1, DDA_y1 = 0, 0, 50, 20
    B_x0, B_y0, B_x1, B_y1 = 20, 0, 70, 20
    B_Cx, B_Cy, B_R = 30, 50, 20
    wu_x0, wu_y0, wu_x1, wu_y1 = 40, 0, 90, 20

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Computer graphics lab1')
    screen = pygame.Surface((window_width, window_height))
    screen.fill(screen_color)

    app_running = True
    while app_running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                app_running = False

        window.blit(screen, (0, 0))
        DDA_line(screen, DDA_x0, DDA_y0, DDA_x1, DDA_y1, draw_color)
        pygame.display.flip()


def TurnOnBresenhamLine(event):
    if __name__ == "__main__":
        main()

def TurnOnBresenhamCircle(event):
    drawCircle(100, 100, 60)

def TurnOnWuLine(event):
    window_width = 1024
    window_height = 768

    screen_color = (255, 255, 255)
    draw_color = (255, 0, 0)

    DDA_x0, DDA_y0, DDA_x1, DDA_y1 = 0, 0, 50, 20
    B_x0, B_y0, B_x1, B_y1 = 20, 0, 70, 20
    B_Cx, B_Cy, B_R = 30, 50, 20
    wu_x0, wu_y0, wu_x1, wu_y1 = 0, 0, 150, 100

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Computer graphics lab1')
    screen = pygame.Surface((window_width, window_height))
    screen.fill(screen_color)

    app_running = True
    while app_running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                app_running = False

        window.blit(screen, (0, 0))
        Wu_line(screen, wu_x0, wu_y0, wu_x1, wu_y1, draw_color)
        pygame.display.flip()

def TurnOnName(event):
    window_width = 800
    window_height = 600

    screen_color = (255, 255, 255)
    draw_color = (255, 0, 0)

    DDA_x0, DDA_y0, DDA_x1, DDA_y1 = 0, 0, 50, 20
    B_x0, B_y0, B_x1, B_y1 = 20, 0, 70, 20
    B_Cx, B_Cy, B_R = 30, 50, 20
    wu_x0, wu_y0, wu_x1, wu_y1 = 40, 0, 90, 20

    window = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('Computer graphics lab1')
    screen = pygame.Surface((window_width, window_height))
    screen.fill(screen_color)

    app_running = True
    while app_running:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                app_running = False

        window.blit(screen, (0, 0))
        name_draw(screen, draw_color)
        pygame.display.flip()

def numdo():
    selection = "Ti vibrav knopku №", str(var.get())
    label.config(text = selection)
    return var.get()

root = Tk()
#Menubar
menubar = Menu(root)
#----AboutMenu
aboutmenu = Menu(menubar, tearoff = 0)
aboutmenu.add_command(label = "DDA", command = donothing)
aboutmenu.add_command(label = "Bresenham", command = donothing)
aboutmenu.add_command(label = "Vu", command = donothing)
menubar.add_cascade(label = "About", menu = aboutmenu)
#----HelpMenu
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "What should I do in this program?", command = donothing)
menubar.add_cascade(label = "Help", menu = helpmenu)
root.config(menu = menubar)



    #button which turns on my final function
but = Button(root,text="DDA line",
                      width = 100, height = 3,
                      bg = "yellow", fg = "blue")
but.bind("<Button-1>", TurnOnDDA)
but.pack()


but1 = Button(root,text="Bresenham line",
                      width = 100, height = 3,
                      bg = "blue", fg = "yellow")
but1.bind("<Button-1>", TurnOnBresenhamLine)
but1.pack()


but2 = Button(root,text="Bresenham circle",
                      width = 100, height = 3,
                      bg = "yellow", fg = "blue")
but2.bind("<Button-1>", TurnOnBresenhamCircle)
but2.pack()


but3 = Button(root,text="Wu line",
                      width = 100, height = 3,
                      bg = "blue", fg = "yellow")
but3.bind("<Button-1>", TurnOnWuLine)
but3.pack()


but4 = Button(root,text="My name",
                      width = 100, height = 3,
                      bg = "yellow", fg = "blue")
but4.bind("<Button-1>", TurnOnName)
but4.pack()

root.mainloop()

