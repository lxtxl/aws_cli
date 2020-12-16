#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/put-profile-object.html
if __name__ == '__main__':
    """
	delete-profile-object : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/delete-profile-object.html
	list-profile-objects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/list-profile-objects.html
    """

    parameter_display_string = """
    # object-type-name : The name of the profile object type.
    # object : A string that is serialized from a JSON object.
    # domain-name : The unique name of the domain.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("customer-profiles", "put-profile-object", "object-type-name", "object", "domain-name", add_option_dict)
