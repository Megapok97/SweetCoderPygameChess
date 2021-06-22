import pygame as pg
from game_config import *
pg.init()
fnt_num = pg.font.Font(FNT_PATH, FNT_SIZE)


class Chessboard:
    def __init__(self, parent_sufface: pg.Surface,
                 cell_qty: int = CELL_QTY, cell_size: int = CELL_SIZE):
        self.__screen = parent_sufface
        self.__qty = cell_qty
        self.__size = cell_size
        self.__all_cells = pg.sprite.Group()
        self.__prepare_screen()
        self.__draw_playboard()
        pg.display.update()

    def __prepare_screen(self):
        back_img = pg.image.load(IMG_PATH + WIN_BG_IMG)
        back_img = pg.transform.scale(back_img, WINDOW_SIZE)
        self.__screen.blit(back_img, (0, 0))

    def __draw_playboard(self):
        total_width = self.__qty * self.__size
        num_filds = self.__create_num_fields()
        self.__all_cells = self.__create_all_cells()
        num_fields_depth = num_filds[0].get_width()
        playboard_view = pg.Surface((
            2 * num_fields_depth + total_width,
            2 * num_fields_depth + total_width
        ), pg.SRCALPHA)

        back_img = pg.image.load(IMG_PATH + BOARD_BG_IMG)
        back_img = pg.transform.scale(back_img, (
            playboard_view.get_width(),
            playboard_view.get_height()
        ))
        playboard_view.blit(back_img, (back_img.get_rect()))

        playboard_view.blit(num_filds[0],
                            (0, num_fields_depth))
        playboard_view.blit(num_filds[0],
                            (num_fields_depth + total_width, num_fields_depth))
        playboard_view.blit(num_filds[1],
                            (num_fields_depth, 0))
        playboard_view.blit(num_filds[1],
                            (num_fields_depth, num_fields_depth + total_width))

        playboard_rect = playboard_view.get_rect()
        playboard_rect.x += (self.__screen.get_width() - playboard_rect.width) // 2
        playboard_rect.y += (self.__screen.get_height() - playboard_rect.height) // 2
        self.__screen.blit(playboard_view, playboard_rect)
        cells_offset = (
            playboard_rect.x + num_fields_depth,
            playboard_rect.y + num_fields_depth
        )
        self.__draw_cells_on_playboard(cells_offset)

    def __create_num_fields(self):
        n_lines = pg.Surface((self.__qty * self.__size, self.__size // 3), pg.SRCALPHA)
        n_rows = pg.Surface((self.__size // 3, self.__qty * self.__size), pg.SRCALPHA)
        for i in range(0, self.__qty):
            letter = fnt_num.render(LTRS[i], True, WHITE)
            number = fnt_num.render(str(self.__qty - i), True, WHITE)
            n_lines.blit(letter, (
                i * self.__size + (self.__size - letter.get_rect().width) // 2,  # X
                (n_lines.get_height() - letter.get_rect().height) // 2  # Y
                )
            )
            n_rows.blit(number, (
                (n_rows.get_width() - letter.get_rect().width) // 2,  # X
                i * self.__size + (self.__size - number.get_rect().height) // 2  # Y
                )
            )
        return n_rows, n_lines

    def __create_all_cells(self):
        group = pg.sprite.Group()
        is_even_qty = (self.__qty % 2 == 0)
        cell_color_index = 1 if is_even_qty else 0

        cell_black = pg.image.load(IMG_PATH + COLORS[0])
        cell_white = pg.image.load(IMG_PATH + COLORS[1])
        cell_black = pg.transform.scale(cell_black, (self.__size, self.__size))
        cell_white = pg.transform.scale(cell_white, (self.__size, self.__size))
        cells = [cell_black, cell_white]

        for y in range(self.__qty):
            for x in range(self.__qty):
                cell = Cell(
                    cell_color_index,
                    self.__size,
                    (x, y),
                    LTRS[x] + str(self.__qty - y)
                )
                group.add(cell)
                cell_color_index ^= True
            cell_color_index = cell_color_index ^ True if is_even_qty else cell_color_index
        return group

    def __draw_cells_on_playboard(self, offset):
        for cell in self.__all_cells:
            cell.rect.x += offset[0]
            cell.rect.y += offset[1]
        self.__all_cells.draw(self.__screen)


class Cell(pg.sprite.Sprite):
    def __init__(self, color_index: int, size: int, coords: tuple, name: str):
        super().__init__()
        x, y = coords
        self.color = color_index
        self.field_name = name
        self.image = pg.image.load(IMG_PATH + COLORS[color_index])
        self.image = pg.transform.scale(self.image, (size, size))
        self.rect = pg.Rect(x * size, y * size, size, size)
