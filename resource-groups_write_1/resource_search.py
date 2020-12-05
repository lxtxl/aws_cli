#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/search-resources.html
if __name__ == '__main__':
    """
	group-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/group-resources.html
	ungroup-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resource-groups/ungroup-resources.html
    """

    parameter_display_string = """
    # resource-query : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("resource-groups", "search-resources", "resource-query", add_option_dict)





