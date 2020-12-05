#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/delete-directory.html
if __name__ == '__main__':
    """
	connect-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/connect-directory.html
	create-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-directory.html
	describe-directories : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-directories.html
	share-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/share-directory.html
	unshare-directory : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/unshare-directory.html
    """

    parameter_display_string = """
    # directory-id : The identifier of the directory to delete.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("ds", "delete-directory", "directory-id", add_option_dict)





