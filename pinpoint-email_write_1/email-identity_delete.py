#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/delete-email-identity.html
if __name__ == '__main__':
    """
	create-email-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/create-email-identity.html
	get-email-identity : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-email-identity.html
	list-email-identities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/list-email-identities.html
    """

    parameter_display_string = """
    # email-identity : The identity (that is, the email address or domain) that you want to delete from your Amazon Pinpoint account.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("pinpoint-email", "delete-email-identity", "email-identity", add_option_dict)





