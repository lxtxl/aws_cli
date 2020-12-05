#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/delete-application.html
if __name__ == '__main__':
    """
	create-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-application.html
	get-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/get-application.html
	list-applications : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/list-applications.html
	unshare-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/unshare-application.html
	update-application : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/update-application.html
    """

    parameter_display_string = """
    # application-id : The Amazon Resource Name (ARN) of the application.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("serverlessrepo", "delete-application", "application-id", add_option_dict)





