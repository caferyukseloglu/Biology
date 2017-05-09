from Tkinter import *
import plot
import random
import pp_sim

number_of_grass = 100
grass_multiply_rate = 2
grass_max_life = 2

number_of_rabbits = 50
rabbit_multiply_rate = 0.5
rabbit_max_speed = 5
rabbit_range_of_vision = 50

number_of_foxes = 20
fox_multiply_rate = 0.5
fox_max_speed = 7
fox_max_steps = 25


cw = 800
ch = 600

r = list()
f = list()

for i in range(0, number_of_rabbits):
    x = random.uniform(0, cw)
    y = random.uniform(0, ch - 180)
    r.append(pp_sim.rabbit(rabbit_max_speed, x, y, cw,
                            ch - 180, rabbit_range_of_vision))

for i in range(0, number_of_foxes):
    x = random.uniform(0, cw)
    y = random.uniform(0, ch - 180)
    f.append(pp_sim.fox(fox_max_speed, fox_max_steps, x, y, cw, ch - 180))

root = Tk()
root.title("Predator and Pray Simulator Biology")

chart_1 = Canvas(root, width=cw, height=ch, background="white")
chart_1.grid(row=0, column=0)

pl = plot.plot()

gn = 0

while 1:
    gn = gn + 1

    chart_1.create_line(0, ch - 173, cw, ch - 173, fill='black')


        
    for i in range(0, len(r)):
        chart_1.create_oval(r[i].x - 5, r[i].y - 5,
                            r[i].x + 5, r[i].y + 5,
                            fill='red')
        r[i].move(f)

    t = list()
    tmp_f = list()
    for i in range(0, len(f)):
        chart_1.create_oval(f[i].x - 5, f[i].y - 5,
                            f[i].x + 5, f[i].y + 5,
                            fill='blue')

        min_i = f[i].move(r)
        if min_i != -1:
            t.append(min_i)
            f[i].steps = 0

        if f[i].steps <= f[i].mx_steps:
            tmp_f.append(f[i])

    p = list()
    t = list(set(t))
    tmp = list()
    for i in range(0, len(r)):
        if i not in t:
            tmp.append(r[i])

    r = tmp[:]
    f = tmp_f[:]
    
    if gn > 25:
        pl.add1(len(r))
        pl.add2(len(f))


        for i in range(0, int(len(r) * rabbit_multiply_rate) + 1):
            x = random.uniform(0, cw)
            y = random.uniform(0, ch - 190)
            r.append(pp_sim.rabbit(rabbit_max_speed, x, y,
                                cw, ch - 180, rabbit_range_of_vision))

        for i in range(0, int(len(f) * fox_multiply_rate) + 1):
            x = random.uniform(0, cw)
            y = random.uniform(0, ch - 190)
            f.append(pp_sim.fox(fox_max_speed, fox_max_steps,
                                x, y, cw, ch - 180))

        gn = 0

    for x in range(0, pl.pointer2 - 2):
        y1 = 150 - pl.nlst1[x] + ch - 170
        y2 = 150 - pl.nlst1[x + 1] + ch - 170
        chart_1.create_line(x * (cw / 100), y1,
                            (x + 1) * 6, y2,
                            fill='red')

        y1 = 150 - pl.nlst2[x] + ch - 170
        y2 = 150 - pl.nlst2[x + 1] + ch - 170
        chart_1.create_line(x * 6, y1,
                            (x + 1) * (cw / 100), y2,
                            fill='blue')

    chart_1.update()
    chart_1.after(20)

    chart_1.delete(ALL)
root.mainloop()
