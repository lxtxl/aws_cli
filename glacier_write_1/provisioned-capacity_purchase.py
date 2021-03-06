#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/purchase-provisioned-capacity.html
if __name__ == '__main__':
    """
	list-provisioned-capacity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glacier/list-provisioned-capacity.html
    """

    parameter_display_string = """
    # account-id : The AWS account ID of the account that owns the vault. You can either specify an AWS account ID or optionally a single â-â (hyphen), in which case Amazon S3 Glacier uses the AWS account ID associated with the credentials used to sign the request. If you use an account ID, donât include any hyphens (â-â) in the ID.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("glacier", "purchase-provisioned-capacity", "account-id", add_option_dict)





