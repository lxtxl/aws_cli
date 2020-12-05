#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-portal.html
if __name__ == '__main__':
    """
	create-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-portal.html
	describe-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-portal.html
	list-portals : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-portals.html
	update-portal : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-portal.html
    """

    parameter_display_string = """
    # portal-id : The ID of the portal to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("iotsitewise", "delete-portal", "portal-id", add_option_dict)





