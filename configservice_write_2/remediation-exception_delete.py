#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/delete-remediation-exceptions.html
if __name__ == '__main__':
    """
	describe-remediation-exceptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-remediation-exceptions.html
	put-remediation-exceptions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-remediation-exceptions.html
    """

    parameter_display_string = """
    # config-rule-name : The name of the AWS Config rule for which you want to delete remediation exception configuration.
    # resource-keys : An exception list of resource exception keys to be processed with the current request. AWS Config adds exception for each resource key. For example, AWS Config adds 3 exceptions for 3 resource keys.
(structure)

The details that identify a resource within AWS Config, including the resource type and resource ID.
ResourceType -> (string)

The type of a resource.

ResourceId -> (string)

The ID of the resource (for example., sg-xxxxxx).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("configservice", "delete-remediation-exceptions", "config-rule-name", "resource-keys", add_option_dict)
