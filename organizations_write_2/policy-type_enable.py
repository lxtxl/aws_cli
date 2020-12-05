#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/enable-policy-type.html
if __name__ == '__main__':
    """
	disable-policy-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/disable-policy-type.html
    """

    parameter_display_string = """
    # root-id : The unique identifier (ID) of the root in which you want to enable a policy type. You can get the ID from the  ListRoots operation.
The regex pattern for a root ID string requires âr-â followed by from 4 to 32 lowercase letters or digits.
    # policy-type : The policy type that you want to enable. You can specify one of the following values:

AISERVICES_OPT_OUT_POLICY
BACKUP_POLICY
SERVICE_CONTROL_POLICY
TAG_POLICY

Possible values:

SERVICE_CONTROL_POLICY
TAG_POLICY
BACKUP_POLICY
AISERVICES_OPT_OUT_POLICY
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("organizations", "enable-policy-type", "root-id", "policy-type", add_option_dict)
