#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/download-db-log-file-portion.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # db-instance-identifier : The customer-assigned name of the DB instance that contains the log files you want to list.
Constraints:

Must match the identifier of an existing DBInstance.
    # log-file-name : The name of the log file to be downloaded.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("rds", "download-db-log-file-portion", "db-instance-identifier", "log-file-name", add_option_dict)
