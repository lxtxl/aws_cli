#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-app-instance-admin.html
if __name__ == '__main__':
    """
	create-app-instance-admin : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-app-instance-admin.html
	describe-app-instance-admin : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-app-instance-admin.html
	list-app-instance-admins : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-app-instance-admins.html
    """

    parameter_display_string = """
    # app-instance-admin-arn : The ARN of the app instanceâs administrator.
    # app-instance-arn : The ARN of the app instance.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("chime", "delete-app-instance-admin", "app-instance-admin-arn", "app-instance-arn", add_option_dict)
