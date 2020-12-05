#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-vpc-association-authorizations.html
if __name__ == '__main__':
    """
	create-vpc-association-authorization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-vpc-association-authorization.html
	delete-vpc-association-authorization : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-vpc-association-authorization.html
    """

    parameter_display_string = """
    # hosted-zone-id : The ID of the hosted zone for which you want a list of VPCs that can be associated with the hosted zone.
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

    execute_one_parameter("route53", "list-vpc-association-authorizations", "hosted-zone-id", add_option_dict)