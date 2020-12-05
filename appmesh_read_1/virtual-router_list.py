#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/list-virtual-routers.html
if __name__ == '__main__':
    """
	create-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/create-virtual-router.html
	delete-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/delete-virtual-router.html
	describe-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/describe-virtual-router.html
	update-virtual-router : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appmesh/update-virtual-router.html
    """

    parameter_display_string = """
    # mesh-name : The name of the service mesh to list virtual routers in.
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("appmesh", "list-virtual-routers", "mesh-name", add_option_dict)