#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/batch-create-table-rows.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # workbook-id : The ID of the workbook where the new rows are being added.
If a workbook with the specified ID could not be found, this API throws ResourceNotFoundException.
    # table-id : The ID of the table where the new rows are being added.
If a table with the specified ID could not be found, this API throws ResourceNotFoundException.
    # rows-to-create : The list of rows to create at the end of the table. Each item in this list needs to have a batch item id to uniquely identify the element in the request and the cells to create for that row. You need to specify at least one item in this list.
Note that if one of the column ids in any of the rows in the request does not exist in the table, then the request fails and no updates are made to the table.
(structure)

Data needed to create a single row in a table as part of the BatchCreateTableRows request.
batchItemId -> (string)

An external identifier that represents the single row that is being created as part of the BatchCreateTableRows request. This can be any string that you can use to identify the row in the request. The BatchCreateTableRows API puts the batch item id in the results to allow you to link data in the request to data in the results.

cellsToCreate -> (map)

A map representing the cells to create in the new row. The key is the column id of the cell and the value is the CellInput object that represents the data to set in that cell.
key -> (string)
value -> (structure)

CellInput object contains the data needed to create or update cells in a table.
fact -> (string)

Fact represents the data that is entered into a cell. This data can be free text or a formula. Formulas need to start with the equals (=) sign.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("honeycode", "batch-create-table-rows", "workbook-id", "table-id", "rows-to-create", add_option_dict)
