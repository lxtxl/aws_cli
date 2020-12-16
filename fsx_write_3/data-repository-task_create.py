#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-data-repository-task.html
if __name__ == '__main__':
    """
	cancel-data-repository-task : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/cancel-data-repository-task.html
	describe-data-repository-tasks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-data-repository-tasks.html
    """

    parameter_display_string = """
    # type : Specifies the type of data repository task to create.
Possible values:

EXPORT_TO_REPOSITORY
    # file-system-id : The globally unique ID of the file system, assigned by Amazon FSx.
    # report : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("fsx", "create-data-repository-task", "type", "file-system-id", "report", add_option_dict)
