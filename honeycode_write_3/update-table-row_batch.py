#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/batch-update-table-rows.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # workbook-id : The ID of the workbook where the rows are being updated.
If a workbook with the specified id could not be found, this API throws ResourceNotFoundException.
    # table-id : The ID of the table where the rows are being updated.
If a table with the specified id could not be found, this API throws ResourceNotFoundException.
    # rows-to-update : The list of rows to update in the table. Each item in this list needs to contain the row id to update along with the map of column id to cell values for each column in that row that needs to be updated. You need to specify at least one row in this list, and for each row, you need to specify at least one column to update.
Note that if one of the row or column ids in the request does not exist in the table, then the request fails and no updates are made to the table.
(structure)

Data needed to create a single row in a table as part of the BatchCreateTableRows request.
rowId -> (string)

The id of the row that needs to be updated.

cellsToUpdate -> (map)

A map representing the cells to update in the given row. The key is the column id of the cell and the value is the CellInput object that represents the data to set in that cell.
key -> (string)
value -> (structure)

CellInput object contains the data needed to create or update cells in a table.
fact -> (string)

Fact represents the data that is entered into a cell. This data can be free text or a formula. Formulas need to start with the equals (=) sign.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("honeycode", "batch-update-table-rows", "workbook-id", "table-id", "rows-to-update", add_option_dict)
