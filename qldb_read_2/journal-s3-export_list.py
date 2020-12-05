#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/describe-journal-s3-export.html
if __name__ == '__main__':
    """
	list-journal-s3-exports : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qldb/list-journal-s3-exports.html
    """

    parameter_display_string = """
    # name : The name of the ledger.
    # export-id : The unique ID of the journal export job that you want to describe.
    """

    execute_two_parameter("qldb", "describe-journal-s3-export", "name", "export-id", parameter_display_string)