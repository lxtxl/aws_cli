#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/accept-shared-directory.html
if __name__ == '__main__':
    """
	describe-shared-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-shared-directories.html
	reject-shared-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/reject-shared-directory.html
    """

    parameter_display_string = """
    # shared-directory-id : Identifier of the shared directory in the directory consumer account. This identifier is different for each directory owner account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ds", "accept-shared-directory", "shared-directory-id", add_option_dict)





