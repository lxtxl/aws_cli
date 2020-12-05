#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/accept-resource-share-invitation.html
if __name__ == '__main__':
    """
	get-resource-share-invitations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-share-invitations.html
	reject-resource-share-invitation : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/reject-resource-share-invitation.html
    """

    parameter_display_string = """
    # resource-share-invitation-arn : The Amazon Resource Name (ARN) of the invitation.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ram", "accept-resource-share-invitation", "resource-share-invitation-arn", add_option_dict)





