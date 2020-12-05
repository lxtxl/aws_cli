#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-inventory.html
if __name__ == '__main__':
    """
	get-inventory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-inventory.html
	put-inventory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-inventory.html
    """

    parameter_display_string = """
    # type-name : The name of the custom inventory type for which you want to delete either all previously collected data or the inventory type itself.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ssm", "delete-inventory", "type-name", add_option_dict)





