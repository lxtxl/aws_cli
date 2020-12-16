#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/modify-backup-attributes.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # backup-id : The identifier (ID) of the backup to modify. To find the ID of a backup, use the  DescribeBackups operation.
    # never-expires | --no-never-expires : Specifies whether the service should exempt a backup from the retention policy for the cluster. True exempts a backup from the retention policy. False means the service applies the backup retention policy defined at the cluster.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("cloudhsmv2", "modify-backup-attributes", "backup-id", "never-expires | --no-never-expires", add_option_dict)
