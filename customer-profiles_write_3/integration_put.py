#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/put-integration.html
if __name__ == '__main__':
    """
	delete-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/delete-integration.html
	get-integration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-integration.html
	list-integrations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/list-integrations.html
    """

    parameter_display_string = """
    # domain-name : The unique name of the domain.
    # uri : The URI of the S3 bucket or any other type of data source.
    # object-type-name : The name of the profile object type.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("customer-profiles", "put-integration", "domain-name", "uri", "object-type-name", add_option_dict)
