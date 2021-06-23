# NAME          : BRYAN HOOI YU ERN
# EMAIL         : hooibryan@gmail.com
# DATE EDITED   : 23/06/2021

"""
A function that creates and returns an ascii table.

Conditions:
    1) Length of each row will always equal the length of labels (if labels are provided) for the input data
    2) No item in any row will contain an escape character such as \n for the input data
    3) If an item cannot be centered evenly, the extra space character should be to the right of the item (see example 3)
    4) Each column should be made wide enough to fit the longest item, with one space on either side for padding
"""

from typing import Any, List, Optional

def longest_word_length(words, labels=None):
    lengths = []

    if labels is None:
        for col in range(len(words[0])):
            col_longest = 0

            for row in range(len(words)):
                word_length = len(str(words[row][col]))
                if word_length > col_longest:
                    col_longest = word_length

            lengths.append(col_longest)

    else:
        for col in range(len(words[0])):
            col_longest = 0

            for row in range(len(words)):
                word_length = len(str(words[row][col]))
                if word_length > col_longest:
                    col_longest = word_length

            if len(str(labels[col])) > col_longest:
                col_longest = len(str(labels[col]))
            lengths.append(col_longest)

    return lengths

def generate_header_footer(column_widths, labels, centered, borders, top=True):
    return_string = ""
    if top:
        return_string += borders["top_left"]
        if labels is None:
            for i in range(len(column_widths)):
                current_width = column_widths[i]
                if i == len(column_widths) - 1:
                    return_string += borders["horizontal_bar"] * (current_width + 2) + borders["top_right"] + "\n"
                else:
                    return_string += borders["horizontal_bar"] * (current_width + 2) + borders["top_centre"]
        else:
            if centered:
                for i in range(len(column_widths)):
                    current_width = column_widths[i]
                    if i == len(column_widths) - 1:
                        return_string += borders["horizontal_bar"] * (current_width + 2) + borders["top_right"] + "\n"
                    else:
                        return_string += borders["horizontal_bar"] * (current_width + 2) + borders["top_centre"]

                return_string += borders["vertical_bar"]

                for i in range(len(labels)):
                    current_width = column_widths[i]
                    shift_amount = (current_width - len(str(labels[i]))) // 2
                    return_string += " " * (1 + shift_amount) + str(labels[i]) + " " * (current_width - len(str(labels[i])) - shift_amount + 1) + borders["vertical_bar"]
                return_string += "\n" + borders["vertical_left"]

                for i in range(len(column_widths)):
                    current_width = column_widths[i]
                    if i == len(column_widths) - 1:
                        return_string += borders["horizontal_bar"] * (current_width + 2) + borders["vertical_right"] + "\n"
                    else:
                        return_string += borders["horizontal_bar"] * (current_width + 2) + borders["vertical_centre"]
            else:
                for i in range(len(column_widths)):
                    current_width = column_widths[i]
                    if i == len(column_widths) - 1:
                        return_string += borders["horizontal_bar"] * (current_width + 2) + borders["top_right"] + "\n"
                    else:
                        return_string += borders["horizontal_bar"] * (current_width + 2) + borders["top_centre"]

                return_string += borders["vertical_bar"]

                for i in range(len(labels)):
                    current_width = column_widths[i]
                    return_string += " " + str(labels[i]) + " " * (current_width - len(str(labels[i])) + 1) + borders["vertical_bar"]
                return_string += "\n" + borders["vertical_left"]

                for i in range(len(column_widths)):
                    current_width = column_widths[i]
                    if i == len(column_widths) - 1:
                        return_string += borders["horizontal_bar"] * (current_width + 2) + borders["vertical_right"] + "\n"
                    else:
                        return_string += borders["horizontal_bar"] * (current_width + 2) + borders["vertical_centre"]
        return return_string
    else:
        return_string += borders["bottom_left"]

        for i in range(len(column_widths)):
            current_width = column_widths[i]
            if i == len(column_widths) - 1:
                return_string += borders["horizontal_bar"] * (current_width + 2) + borders["bottom_right"]
            else:
                return_string += borders["horizontal_bar"] * (current_width + 2) + borders["bottom_centre"]

        return return_string

def generate_rows(words, column_widths, centered, borders):
    return_string = borders["vertical_bar"]
    if centered:
        for i in range(len(words)):
            for j in range(len(words[i])):
                current_width = column_widths[j]
                shift_amount = (current_width - len(str(words[i][j]))) // 2
                return_string += " " * (1 + shift_amount) + str(words[i][j]) + " " * (
                            current_width - len(str(words[i][j])) - shift_amount + 1) + borders["vertical_bar"]
            if i != len(words) - 1:
                return_string += "\n" + borders["vertical_bar"]
            else:
                return_string += "\n"
    else:
        for i in range(len(words)):
            for j in range(len(words[i])):
                current_width = column_widths[j]
                return_string += " " + str(words[i][j]) + " " * (current_width - len(str(words[i][j])) + 1) + borders["vertical_bar"]
            if i != len(words) - 1:
                return_string += "\n" + borders["vertical_bar"]
            else:
                return_string += "\n"

    return return_string

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """

    borders = {"vertical_bar": "│", "horizontal_bar": "─", "top_left": "┌", "top_centre": "┬", "top_right": "┐",
               "vertical_left": "├", "vertical_centre": "┼", "vertical_right": "┤", "bottom_left": "└",
               "bottom_centre": "┴",
               "bottom_right": "┘"}

    table = ""
    column_widths = longest_word_length(rows, labels)
    table += generate_header_footer(column_widths, labels, centered, borders) + generate_rows(rows, column_widths, centered, borders) + generate_header_footer(column_widths, labels, centered, borders, False)

    return table
