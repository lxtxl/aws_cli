#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-app-instance-user.html
if __name__ == '__main__':
    """
	create-app-instance-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-app-instance-user.html
	describe-app-instance-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-app-instance-user.html
	list-app-instance-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-app-instance-users.html
	update-app-instance-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-app-instance-user.html
    """

    parameter_display_string = """
    # app-instance-user-arn : The ARN of the user request being deleted.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("chime", "delete-app-instance-user", "app-instance-user-arn", add_option_dict)





