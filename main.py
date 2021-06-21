import pygame as pg

xyz = "git pidor"


pg.init()
clock = pg.time.Clock()
FPS = 30
WINDOW_SIZE = (800, 800)
BACKGROUND = (150, 90, 30)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
YELLOW = (255, 255, 0)
CELL_QTY = 8
CELL_SIZE = 70
COLORS = [YELLOW, GREY]
FNT18 = pg.font.Font('assets/fonts/Arial.ttf', 18)
LTRS = 'abcdefghijklmnopqrstuvwxyz'
screen = pg.display.set_mode(WINDOW_SIZE)

# 321
MID_GRAY = (90, 90, 90)
FNT28 = pg.font.Font('assets/fonts/Arial.ttf', 18)
#  123
screen.fill(BACKGROUND)

n_lines = pg.Surface((CELL_QTY * CELL_SIZE, CELL_SIZE // 2)).convert_alpha()
n_rows = pg.Surface((CELL_SIZE // 2, CELL_QTY * CELL_SIZE)).convert_alpha()
fields = pg.Surface((CELL_QTY * CELL_SIZE, CELL_QTY * CELL_SIZE)).convert_alpha()
board = pg.Surface((
    2 * n_rows.get_width() + fields.get_width(),
    2 * n_lines.get_height() + fields.get_height()
)).convert_alpha()

is_even_qty = (CELL_QTY % 2 == 0)
cell_color_index = 1 if is_even_qty else 0
for y in range(CELL_QTY):
    for x in range(CELL_QTY):
        # pg.draw.rect(screen, COLORS[cell_color_index], (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        cell = pg.Surface((CELL_SIZE, CELL_SIZE)).convert_alpha()
        cell.fill(COLORS[cell_color_index])

        cell_name = FNT28.render(LTRS[x] + str(CELL_QTY - y), True, MID_GRAY)
        cell.blit(cell_name, (
            (CELL_SIZE - cell_name.get_rect().width) // 2,
            (CELL_SIZE - cell_name.get_rect().height) // 2
        ))

        fields.blit(cell, (x * CELL_SIZE, y * CELL_SIZE))
        cell_color_index ^= True
    cell_color_index = cell_color_index ^ True if is_even_qty else cell_color_index

for i in range(0, CELL_QTY):
    letter = FNT18.render(LTRS[i], True, WHITE)
    number = FNT18.render(str(CELL_QTY - i), True, WHITE)
    n_lines.blit(letter, (
        i * CELL_SIZE + (CELL_SIZE - letter.get_rect().width) // 2,  # X
        (n_lines.get_height() - letter.get_rect().height) // 2  # Y
        )
    )
    n_rows.blit(number, (
        (n_rows.get_width() - letter.get_rect().width) // 2,  # X
        i * CELL_SIZE + (CELL_SIZE - number.get_rect().height) // 2  # Y
        )
    )

board.blit(n_rows, (0, n_lines.get_height()))
board.blit(n_rows, (n_rows.get_width() + fields.get_width(), n_lines.get_height()))
board.blit(n_lines, (n_rows.get_width(), 0))
board.blit(n_lines, (n_rows.get_width(), n_rows.get_width() + fields.get_width()))
board.blit(fields, (n_rows.get_width(), n_lines.get_height()))
screen.blit(board, (
    (WINDOW_SIZE[0] - board.get_width()) // 2,
    (WINDOW_SIZE[1] - board.get_height()) // 2
    )
)

rect1 = pg.draw.rect(screen, BLACK, (fields.get_rect()))

pg.display.update()

run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    clock.tick(FPS)
pg.quit()
