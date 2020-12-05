#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-on-premises-instance.html
if __name__ == '__main__':
    """
	deregister-on-premises-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/deregister-on-premises-instance.html
	list-on-premises-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-on-premises-instances.html
	register-on-premises-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register-on-premises-instance.html
    """

    parameter_display_string = """
    # instance-name : The name of the on-premises instance about which to get information.
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

    execute_one_parameter("deploy", "get-on-premises-instance", "instance-name", add_option_dict)