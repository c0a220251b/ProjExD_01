import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png") #練習1
    tmr = 0
    kk_hanten = pg.transform.flip(kk_img, True, False) #練習2 画像の反転
    #練習3　画像の回転
    kk_imgs = [pg.transform.rotozoom(kk_hanten, i, 1.0) for i in range(11)]
    c = [0,1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1,0]
    bg_img_hanten = pg.transform.flip(bg_img, True, False)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return     
        x = tmr%3200  #練習6　動く背景画像
        screen.blit(bg_img, [-x, 0]) #練習4
        screen.blit(bg_img_hanten, [1600-x, 0])
        screen.blit(bg_img, [3200-x, 0]) #課題2
        screen.blit(kk_imgs[c[tmr%20]], [300, 200]) #練習5
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()