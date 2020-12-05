#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/update-enrollment-status.html
if __name__ == '__main__':
    """
	get-enrollment-status : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/compute-optimizer/get-enrollment-status.html
    """

    parameter_display_string = """
    # status : The new enrollment status of the account.
Accepted options are Active or Inactive . You will get an error if Pending or Failed are specified.
Possible values:

Active
Inactive
Pending
Failed
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("compute-optimizer", "update-enrollment-status", "status", add_option_dict)





