#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/start-remediation-execution.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # config-rule-name : The list of names of AWS Config rules that you want to run remediation execution for.
    # resource-keys : A list of resource keys to be processed with the current request. Each element in the list consists of the resource type and resource ID.
(structure)

The details that identify a resource within AWS Config, including the resource type and resource ID.
resourceType -> (string)

The resource type.

resourceId -> (string)

The ID of the resource (for example., sg-xxxxxx).
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("configservice", "start-remediation-execution", "config-rule-name", "resource-keys", add_option_dict)
