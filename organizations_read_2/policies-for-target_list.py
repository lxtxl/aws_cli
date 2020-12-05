#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/organizations/list-policies-for-target.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # target-id : The unique identifier (ID) of the root, organizational unit, or account whose policies you want to list.
The regex pattern for a target ID string requires one of the following:

Root - A string that begins with âr-â followed by from 4 to 32 lowercase letters or digits.
Account - A string that consists of exactly 12 digits.
Organizational unit (OU) - A string that begins with âou-â followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second â-â dash and from 8 to 32 additional lowercase letters or digits.
    # filter : The type of policy that you want to include in the returned list. You must specify one of the following values:

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

    execute_two_parameter("organizations", "list-policies-for-target", "target-id", "filter", parameter_display_string)