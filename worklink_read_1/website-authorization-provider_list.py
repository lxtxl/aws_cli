#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-website-authorization-providers.html
if __name__ == '__main__':
    """
	associate-website-authorization-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/associate-website-authorization-provider.html
	disassociate-website-authorization-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/disassociate-website-authorization-provider.html
    """

    parameter_display_string = """
    # fleet-arn : The ARN of the fleet.
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

    execute_one_parameter("worklink", "list-website-authorization-providers", "fleet-arn", add_option_dict)