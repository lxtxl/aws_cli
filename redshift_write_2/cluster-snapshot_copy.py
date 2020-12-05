#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/copy-cluster-snapshot.html
if __name__ == '__main__':
    """
	create-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-cluster-snapshot.html
	delete-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-cluster-snapshot.html
	describe-cluster-snapshots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-cluster-snapshots.html
	modify-cluster-snapshot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-cluster-snapshot.html
    """

    parameter_display_string = """
    # source-snapshot-identifier : The identifier for the source snapshot.
Constraints:

Must be the identifier for a valid automated snapshot whose state is available .
    # target-snapshot-identifier : The identifier given to the new manual snapshot.
Constraints:

Cannot be null, empty, or blank.
Must contain from 1 to 255 alphanumeric characters or hyphens.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.
Must be unique for the AWS account that is making the request.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "copy-cluster-snapshot", "source-snapshot-identifier", "target-snapshot-identifier", add_option_dict)
