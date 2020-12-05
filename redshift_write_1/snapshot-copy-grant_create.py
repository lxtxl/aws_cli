#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-snapshot-copy-grant.html
if __name__ == '__main__':
    """
	delete-snapshot-copy-grant : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/delete-snapshot-copy-grant.html
	describe-snapshot-copy-grants : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-snapshot-copy-grants.html
    """

    parameter_display_string = """
    # snapshot-copy-grant-name : The name of the snapshot copy grant. This name must be unique in the region for the AWS account.
Constraints:

Must contain from 1 to 63 alphanumeric characters or hyphens.
Alphabetic characters must be lowercase.
First character must be a letter.
Cannot end with a hyphen or contain two consecutive hyphens.
Must be unique for all clusters within an AWS account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("redshift", "create-snapshot-copy-grant", "snapshot-copy-grant-name", add_option_dict)





