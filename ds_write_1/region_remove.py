#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/remove-region.html
if __name__ == '__main__':
    """
	add-region : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/add-region.html
	describe-regions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-regions.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory for which you want to remove Region replication.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ds", "remove-region", "directory-id", add_option_dict)





