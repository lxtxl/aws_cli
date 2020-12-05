#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/authorize-snapshot-access.html
if __name__ == '__main__':
    """
	revoke-snapshot-access : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/revoke-snapshot-access.html
    """

    parameter_display_string = """
    # snapshot-identifier : The identifier of the snapshot the account is authorized to restore.
    # account-with-restore-access : The identifier of the AWS customer account authorized to restore the specified snapshot.
To share a snapshot with AWS support, specify amazon-redshift-support.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("redshift", "authorize-snapshot-access", "snapshot-identifier", "account-with-restore-access", add_option_dict)
