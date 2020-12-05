#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/replace-route-table-association.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # association-id : The association ID.
    # route-table-id : The ID of the new route table to associate with the subnet.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "replace-route-table-association", "association-id", "route-table-id", add_option_dict)
