#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/associate-admin-account.html
if __name__ == '__main__':
    """
	disassociate-admin-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/disassociate-admin-account.html
	get-admin-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fms/get-admin-account.html
    """

    parameter_display_string = """
    # admin-account : The AWS account ID to associate with AWS Firewall Manager as the AWS Firewall Manager administrator account. This can be an AWS Organizations master account or a member account. For more information about AWS Organizations and master accounts, see Managing the AWS Accounts in Your Organization .
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("fms", "associate-admin-account", "admin-account", add_option_dict)





