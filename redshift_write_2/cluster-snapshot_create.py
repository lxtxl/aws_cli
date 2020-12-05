#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-snapshot.html
if __name__ == '__main__':
    """
	copy-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/copy-cluster-snapshot.html
	delete-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-snapshot.html
	describe-cluster-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-snapshots.html
	modify-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-snapshot.html
    """

    parameter_display_string = """
    # snapshot-identifier : A unique identifier for the snapshot that you are requesting. This identifier must be unique for all snapshots within the AWS account.
Constraints:

Cannot be null, empty, or blank
Must contain from 1 to 255 alphanumeric characters or hyphens
First character must be a letter
Cannot end with a hyphen or contain two consecutive hyphens

Example: my-snapshot-id
    # cluster-identifier : The cluster identifier for which you want a snapshot.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "create-cluster-snapshot", "snapshot-identifier", "cluster-identifier", add_option_dict)
