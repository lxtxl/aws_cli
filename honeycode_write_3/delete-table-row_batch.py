#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/honeycode/batch-delete-table-rows.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # workbook-id : The ID of the workbook where the rows are being deleted.
If a workbook with the specified id could not be found, this API throws ResourceNotFoundException.
    # table-id : The ID of the table where the rows are being deleted.
If a table with the specified id could not be found, this API throws ResourceNotFoundException.
    # row-ids : The list of row ids to delete from the table. You need to specify at least one row id in this list.
Note that if one of the row ids provided in the request does not exist in the table, then the request fails and no rows are deleted from the table.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("honeycode", "batch-delete-table-rows", "workbook-id", "table-id", "row-ids", add_option_dict)
