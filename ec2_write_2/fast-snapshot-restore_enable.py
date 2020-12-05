#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/enable-fast-snapshot-restores.html
if __name__ == '__main__':
    """
	describe-fast-snapshot-restores : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fast-snapshot-restores.html
	disable-fast-snapshot-restores : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-fast-snapshot-restores.html
    """

    parameter_display_string = """
    # availability-zones : One or more Availability Zones. For example, us-east-2a .
(string)
    # source-snapshot-ids : The IDs of one or more snapshots. For example, snap-1234567890abcdef0 . You can specify a snapshot that was shared with you from another AWS account.
(string)
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "enable-fast-snapshot-restores", "availability-zones", "source-snapshot-ids", add_option_dict)
