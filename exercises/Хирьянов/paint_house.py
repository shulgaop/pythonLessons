from graph import *
def main():
    windowsize(600, 500)
    paint_house(200 , 100, 200, 400)
    run()
    
    def paint_house(x, y, width, height):
    
    """paint house (x, y) -- baise(start) point is left down
    """
    paint_walls(x, y, width, height // 2)
    paint_roof(x, y, widht, height // 2)
    w_width = width // 3
    w_height = height // 6
    paint_window(x +w_width, y + w_height, w_width, w_height)

main()
