#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/export-table-to-point-in-time.html
if __name__ == '__main__':
    """
	restore-table-to-point-in-time : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/restore-table-to-point-in-time.html
    """

    parameter_display_string = """
    # table-arn : The Amazon Resource Name (ARN) associated with the table to export.
    # s3-bucket : The name of the Amazon S3 bucket to export the snapshot to.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("dynamodb", "export-table-to-point-in-time", "table-arn", "s3-bucket", add_option_dict)
