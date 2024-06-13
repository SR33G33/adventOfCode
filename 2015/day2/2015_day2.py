def calc_surface_area():
    total = 0
    for line in open("input.txt"):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        area = 2*l*w + 2*w*h + 2*h*l
        slack = min(l*w, w*h, h*l)
        total += area + slack
    return total

def calc_bow():
    total = 0
    for line in open("input.txt"):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        ribbon = 2 * min(l+w, w+h, h+l)
        bow = l*w*h
        total += (ribbon + bow)
    return total

area = calc_surface_area()
print("The paper needed is: ", area)

bow = calc_bow()
print("The bow needed is: ", bow)
