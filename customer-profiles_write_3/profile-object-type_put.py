#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/put-profile-object-type.html
if __name__ == '__main__':
    """
	delete-profile-object-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/delete-profile-object-type.html
	get-profile-object-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-profile-object-type.html
	list-profile-object-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/list-profile-object-types.html
    """

    parameter_display_string = """
    # domain-name : The unique name of the domain.
    # object-type-name : The name of the profile object type.
    # description : Description of the profile object type.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("customer-profiles", "put-profile-object-type", "domain-name", "object-type-name", "description", add_option_dict)
