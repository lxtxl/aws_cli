#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/put-apps-list.html
if __name__ == '__main__':
    """
	delete-apps-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/delete-apps-list.html
	get-apps-list : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-apps-list.html
	list-apps-lists : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/list-apps-lists.html
    """

    parameter_display_string = """
    # apps-list : 
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("fms", "put-apps-list", "apps-list", add_option_dict)





