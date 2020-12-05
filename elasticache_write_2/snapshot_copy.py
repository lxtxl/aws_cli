#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/copy-snapshot.html
if __name__ == '__main__':
    """
	create-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-snapshot.html
	delete-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/delete-snapshot.html
	describe-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/describe-snapshots.html
    """

    parameter_display_string = """
    # source-snapshot-name : The name of an existing snapshot from which to make a copy.
    # target-snapshot-name : A name for the snapshot copy. ElastiCache does not permit overwriting a snapshot, therefore this name must be unique within its context - ElastiCache or an Amazon S3 bucket if exporting.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elasticache", "copy-snapshot", "source-snapshot-name", "target-snapshot-name", add_option_dict)
