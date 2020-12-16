#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/create-profile.html
if __name__ == '__main__':
    """
	delete-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/delete-profile.html
	search-profiles : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/search-profiles.html
	update-profile : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/update-profile.html
    """

    parameter_display_string = """
    # domain-name : The unique name of the domain.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("customer-profiles", "create-profile", "domain-name", add_option_dict)





