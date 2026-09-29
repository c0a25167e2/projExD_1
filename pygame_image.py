import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    tmr = 0
    kk_img = pg.image.load("fig/3.png")#練習３
    kk_img = pg.transform.flip(kk_img, True, False)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = -tmr
        screen.blit(bg_img, [x, 0])#練習５
        screen.blit(kk_img, [300, 200])#練習４
        pg.display.update()
        tmr += 10        
        clock.tick(200)#練習６


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()