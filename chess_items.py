import pygame as pg
from game_config import *
pg.init()
fnt_num = pg.font.Font(FNT_PATH, FNT_SIZE)


class Chessboard:
    def __init__(self, parent_sufface: pg.Surface,
                 cell_qty: int = CELL_QTY, cell_size: int = CELL_SIZE):
        self.__screen = parent_sufface
        self.__draw_playboard(cell_qty, cell_size)
        pg.display.update()

    def __draw_playboard(self, cell_qty, cell_size):
        total_width = cell_qty * cell_size
        num_filds = self.__create_num_fields(cell_qty, cell_size)
        fields = self.__create_all_cells(cell_qty, cell_size)
        num_fields_depth = num_filds[0].get_width()
        playboard_view = pg.Surface((
            2 * num_fields_depth + total_width,
            2 * num_fields_depth + total_width
        ), pg.SRCALPHA)

        playboard_view.blit(num_filds[0],
                            (0, num_fields_depth))
        playboard_view.blit(num_filds[0],
                            (num_fields_depth + total_width, num_fields_depth))
        playboard_view.blit(num_filds[1],
                            (num_fields_depth, 0))
        playboard_view.blit(num_filds[1],
                            (num_fields_depth, num_fields_depth + total_width))
        playboard_view.blit(fields,
                            (num_fields_depth, num_fields_depth))

        playboard_rect = playboard_view.get_rect()
        playboard_rect.x += (self.__screen.get_width() - playboard_rect.width) // 2
        playboard_rect.y += (self.__screen.get_height() - playboard_rect.height) // 2
        self.__screen.blit(playboard_view, playboard_rect)


    def __create_num_fields(self, cell_qty, cell_size):
        n_lines = pg.Surface((cell_qty * cell_size, cell_size // 3), pg.SRCALPHA)
        n_rows = pg.Surface((cell_size // 3, cell_qty * cell_size), pg.SRCALPHA)
        for i in range(0, cell_qty):
            letter = fnt_num.render(LTRS[i], True, WHITE)
            number = fnt_num.render(str(cell_qty - i), True, WHITE)
            n_lines.blit(letter, (
                i * cell_size + (cell_size - letter.get_rect().width) // 2,  # X
                (n_lines.get_height() - letter.get_rect().height) // 2  # Y
                )
            )
            n_rows.blit(number, (
                (n_rows.get_width() - letter.get_rect().width) // 2,  # X
                i * cell_size + (cell_size - number.get_rect().height) // 2  # Y
                )
            )
        return (n_rows, n_lines)


    def __create_all_cells(self, cell_qty, cell_size):
        fields = pg.Surface((cell_qty * cell_size, cell_qty * cell_size))
        is_even_qty = (cell_qty % 2 == 0)
        cell_color_index = 1 if is_even_qty else 0
        for y in range(cell_qty):
            for x in range(cell_qty):
                cell = pg.Surface((cell_size, cell_size), pg.SRCALPHA)
                cell.fill(COLORS[cell_color_index])
                fields.blit(cell, (x * cell_size, y * cell_size))
                cell_color_index ^= True
            cell_color_index = cell_color_index ^ True if is_even_qty else cell_color_index
        return  fields
