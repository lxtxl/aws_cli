#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-snapshot.html
if __name__ == '__main__':
    """
	copy-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/copy-snapshot.html
	create-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-snapshot.html
	describe-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-snapshots.html
    """

    parameter_display_string = """
    # snapshot-name : The name of the snapshot to be deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("elasticache", "delete-snapshot", "snapshot-name", add_option_dict)





