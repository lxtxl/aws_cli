#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-profile-object-type.html
if __name__ == '__main__':
    """
	delete-profile-object-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/delete-profile-object-type.html
	list-profile-object-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/list-profile-object-types.html
	put-profile-object-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/put-profile-object-type.html
    """

    parameter_display_string = """
    # domain-name : The unique name of the domain.
    # object-type-name : The name of the profile object type.
    """

    execute_two_parameter("customer-profiles", "get-profile-object-type", "domain-name", "object-type-name", parameter_display_string)