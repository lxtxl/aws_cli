#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-website-certificate-authorities.html
if __name__ == '__main__':
    """
	associate-website-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/associate-website-certificate-authority.html
	describe-website-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/describe-website-certificate-authority.html
	disassociate-website-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/disassociate-website-certificate-authority.html
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

    execute_one_parameter("worklink", "list-website-certificate-authorities", "fleet-arn", add_option_dict)