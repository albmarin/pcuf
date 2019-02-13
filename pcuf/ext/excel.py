# -*- coding: utf-8 -*-
import re
from datetime import datetime

import pandas
import xlrd
from openpyxl import load_workbook


def load_wb_data(
    path,
    sheet_index: int = 0,
    table_row: int = 0,
    table_col: int = 0,
    invert_direction: bool = False,
) -> dict:
    wb = xlrd.open_workbook(path, on_demand=True)
    ws = wb.sheet_by_index(sheet_index)
    header = []
    data = []

    cols = ws.ncols
    rows = ws.nrows
    table_range = table_row + 1, rows

    if invert_direction:
        cols = ws.nrows
        rows = ws.ncols
        table_range = table_col + 1, rows

    for col in range(cols):
        cell_value = ws.cell_value(table_row, col)

        if invert_direction:
            cell_value = ws.cell_value(col, table_row)

        header.append(" ".join(str(cell_value).split()))

    for row in range(*table_range):
        elm = {}
        for col in range(cols):
            cell_value = ws.cell_value(row, col)
            if invert_direction:
                cell_value = ws.cell_value(col, row)
            elm_key = re.sub(r"[^\w]", "_", header[col].lower()).strip("_")
            elm[elm_key] = cell_value

        data.append(elm)
    return data


def load_wb_cell(path, sheet_index=0, cell="A1"):
    wb = load_workbook(str(path))
    ws_name = wb.sheetnames[sheet_index]
    ws = wb[ws_name]

    return ws[cell].value


def convert_excel_time(excel_time):
    if isinstance(excel_time, float):
        dt = pandas.to_datetime("1899-12-30") + pandas.to_timedelta(excel_time, "D")
        return dt.strftime("%a, %d %b %Y %H:%M:%S -0500")

    if isinstance(excel_time, str):
        try:
            dt = datetime.strptime(excel_time, "%a, %d %b %Y %H:%M:%S %z")
            return dt.strftime("%a, %d %b %Y %H:%M:%S %z")
        except ValueError:
            pass

    return ""
