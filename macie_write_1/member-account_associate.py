#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/associate-member-account.html
if __name__ == '__main__':
    """
	disassociate-member-account : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/disassociate-member-account.html
	list-member-accounts : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie/list-member-accounts.html
    """

    parameter_display_string = """
    # member-account-id : The ID of the AWS account that you want to associate with Amazon Macie Classic as a member account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("macie", "associate-member-account", "member-account-id", add_option_dict)





