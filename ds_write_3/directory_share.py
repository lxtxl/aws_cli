#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/share-directory.html
if __name__ == '__main__':
    """
	connect-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/connect-directory.html
	create-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-directory.html
	delete-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-directory.html
	describe-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-directories.html
	unshare-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/unshare-directory.html
    """

    parameter_display_string = """
    # directory-id : Identifier of the AWS Managed Microsoft AD directory that you want to share with other AWS accounts.
    # share-target : 
    # share-method : The method used when sharing a directory to determine whether the directory should be shared within your AWS organization (ORGANIZATIONS ) or with any AWS account by sending a directory sharing request (HANDSHAKE ).
Possible values:

ORGANIZATIONS
HANDSHAKE
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("ds", "share-directory", "directory-id", "share-target", "share-method", add_option_dict)
