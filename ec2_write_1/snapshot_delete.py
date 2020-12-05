#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-snapshot.html
if __name__ == '__main__':
    """
	copy-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-snapshot.html
	create-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-snapshot.html
	create-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-snapshots.html
	describe-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshots.html
	import-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-snapshot.html
    """

    parameter_display_string = """
    # snapshot-id : The ID of the EBS snapshot.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ec2", "delete-snapshot", "snapshot-id", add_option_dict)





