#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-file-system-from-backup.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # backup-id : The ID of the backup. Specifies the backup to use if youâre creating a file system from an existing backup.
    # subnet-ids : Specifies the IDs of the subnets that the file system will be accessible from. For Windows MULTI_AZ_1 file system deployment types, provide exactly two subnet IDs, one for the preferred file server and one for the standby file server. You specify one of these subnets as the preferred subnet using the WindowsConfiguration > PreferredSubnetID property.
For Windows SINGLE_AZ_1 and SINGLE_AZ_2 deployment types and Lustre file systems, provide exactly one subnet ID. The file server is launched in that subnetâs Availability Zone.
(string)

The ID for a subnet. A subnet is a range of IP addresses in your virtual private cloud (VPC). For more information, see VPC and Subnets in the Amazon VPC User Guide.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("fsx", "create-file-system-from-backup", "backup-id", "subnet-ids", add_option_dict)
