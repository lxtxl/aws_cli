#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/batch-upsert-table-rows.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # workbook-id : The ID of the workbook where the rows are being upserted.
If a workbook with the specified id could not be found, this API throws ResourceNotFoundException.
    # table-id : The ID of the table where the rows are being upserted.
If a table with the specified id could not be found, this API throws ResourceNotFoundException.
    # rows-to-upsert : The list of rows to upsert in the table. Each item in this list needs to have a batch item id to uniquely identify the element in the request, a filter expression to find the rows to update for that element and the cell values to set for each column in the upserted rows. You need to specify at least one item in this list.
Note that if one of the filter formulas in the request fails to evaluate because of an error or one of the column ids in any of the rows does not exist in the table, then the request fails and no updates are made to the table.
(structure)

Data needed to upsert rows in a table as part of a single item in the BatchUpsertTableRows request.
batchItemId -> (string)

An external identifier that represents a single item in the request that is being upserted as part of the BatchUpsertTableRows request. This can be any string that you can use to identify the item in the request. The BatchUpsertTableRows API puts the batch item id in the results to allow you to link data in the request to data in the results.

filter -> (structure)

The filter formula to use to find existing matching rows to update. The formula needs to return zero or more rows. If the formula returns 0 rows, then a new row will be appended in the target table. If the formula returns one or more rows, then the returned rows will be updated.
Note that the filter formula needs to return rows from the target table for the upsert operation to succeed. If the filter formula has a syntax error or it doesnât evaluate to zero or more rows in the target table for any one item in the input list, then the entire BatchUpsertTableRows request fails and no updates are made to the table.
formula -> (string)

A formula representing a filter function that returns zero or more matching rows from a table. Valid formulas in this field return a list of rows from a table. The most common ways of writing a formula to return a list of rows are to use the FindRow() or Filter() functions. Any other formula that returns zero or more rows is also acceptable. For example, you can use a formula that points to a cell that contains a filter function.

contextRowId -> (string)

The optional contextRowId attribute can be used to specify the row id of the context row if the filter formula contains unqualified references to table columns and needs a context row to evaluate them successfully.


cellsToUpdate -> (map)

A map representing the cells to update for the matching rows or an appended row. The key is the column id of the cell and the value is the CellInput object that represents the data to set in that cell.
key -> (string)
value -> (structure)

CellInput object contains the data needed to create or update cells in a table.
fact -> (string)

Fact represents the data that is entered into a cell. This data can be free text or a formula. Formulas need to start with the equals (=) sign.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("honeycode", "batch-upsert-table-rows", "workbook-id", "table-id", "rows-to-upsert", add_option_dict)
