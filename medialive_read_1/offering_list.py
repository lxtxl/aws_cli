#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/describe-offering.html
if __name__ == '__main__':
    """
	list-offerings : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-offerings.html
	purchase-offering : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/purchase-offering.html
    """

    parameter_display_string = """
    # offering-id : Unique offering ID, e.g. â87654321â
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

    execute_one_parameter("medialive", "describe-offering", "offering-id", add_option_dict)