"""
File: babygraphics.py
Name: 
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter as tk
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE+(width // (len(YEARS) - 2)-GRAPH_MARGIN_SIZE)*year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    # The top side of line

    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # The bottom side of line
    '''
    Get the respective coordinate and create vertical line at their x coordinate. And use the intersection point
    to put the year of text on it.
    '''
    for i in range(len(YEARS)):
        line_coordinate = get_x_coordinate(CANVAS_WIDTH, i)
        canvas.create_line(line_coordinate, 0, line_coordinate, CANVAS_HEIGHT)
        canvas.create_text(TEXT_DX+line_coordinate, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, anchor=tk.NW, text=YEARS[i])


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color_count = 0
    for i in range(len(lookup_names)):
        '''
        When every time loop goes, it will have a new index color_count.
        when index out of range of COLORS it will go back yto it's 
        initially value.
        '''
        line_color = COLORS[color_count]
        color_count += 1
        if color_count > len(COLORS) - 1:
            color_count -= len(COLORS)

        for j in range(len(YEARS)-1):
            '''
            In order to draw line, we need to get two points coordinates so that we
            can line it together.
            
            y coordinate: If that year data exist we use a formula to give it
            a y coordinate else we let it's y coordinate be bottom of line.
            
            x coordinate:Using function to get x coordinate in turn
            '''

            pre_data_x = get_x_coordinate(CANVAS_WIDTH, j)
            end_data_x = get_x_coordinate(CANVAS_WIDTH, j+1)
            year_1 = YEARS[j]
            year_2 = YEARS[j + 1]

            if str(year_1) in name_data[lookup_names[i]]:
                rank_1 = name_data[lookup_names[i]][str(year_1)]
                pre_data_y = GRAPH_MARGIN_SIZE + int(rank_1) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)//1000
                # it is a formula to get y coordinate
            else:
                rank_1 = '*'
                pre_data_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                # Can't find data so use * instead and let it's y coordinate at the bottom of line

            if str(year_2) in name_data[lookup_names[i]]:
                rank_2 = name_data[lookup_names[i]][str(year_2)]
                end_data_y = GRAPH_MARGIN_SIZE + int(rank_2) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)//1000
            else:
                rank_2 = '*'
                end_data_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE

            canvas.create_text(TEXT_DX + pre_data_x, pre_data_y, anchor=tk.SW,
                               text=lookup_names[i] + ' ' + rank_1, fill=line_color, font=TEXT_DX)
            canvas.create_line(pre_data_x, pre_data_y, end_data_x, end_data_y, fill=line_color, width=LINE_WIDTH )
            '''
            Because the loop only run 11 times so we need to create text at end to indicate the last year data
            '''
            if j == 10:
                canvas.create_text(TEXT_DX + end_data_x, end_data_y, anchor=tk.SW,
                                   text=lookup_names[i] + ' ' + str(rank_2), fill=line_color, font=TEXT_DX)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tk.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)
    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
