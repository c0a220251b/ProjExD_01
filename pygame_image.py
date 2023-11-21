import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    koka_img = pg.image.load("ex01/fig/3.png") #練習1
    tmr = 0
    hanten = pg.transform.flip(koka_img, True, False)
    kaiten = pg.transform.rotate(koka_img,10)
    koka_lst = [hanten,kaiten]
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0]) #練習4
        # for i in range(len(koka_lst)):
        #     screen.blit(koka_lst[i],[300,200])
        screen.blit((hanten,[300,200]))
        pg.display.update()
        tmr += 1        
        clock.tick(10)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()