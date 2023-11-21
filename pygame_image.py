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
    kk_kaiten = pg.transform.rotozoom(kk_hanten, 10, 1.0) 
    kk_imgs = [kk_hanten, kk_kaiten] #練習3　画像の回転
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return     
        x = tmr%1600  #練習6　動く背景画像
        screen.blit(bg_img, [-x, 0]) #練習4
        screen.blit(bg_img, [1600-x, 0]) 
        screen.blit(kk_imgs[tmr%2], [300, 200]) #練習5
        pg.display.update()
        tmr += 1        
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()