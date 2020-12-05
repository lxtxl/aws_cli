#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/copy-snapshot.html
if __name__ == '__main__':
    """
	create-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-snapshot.html
	create-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-snapshots.html
	delete-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-snapshot.html
	describe-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-snapshots.html
	import-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/import-snapshot.html
    """

    parameter_display_string = """
    # source-region : The ID of the Region that contains the snapshot to be copied.
    # source-snapshot-id : The ID of the EBS snapshot to copy.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("ec2", "copy-snapshot", "source-region", "source-snapshot-id", add_option_dict)
