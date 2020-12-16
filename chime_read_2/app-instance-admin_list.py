#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/describe-app-instance-admin.html
if __name__ == '__main__':
    """
	create-app-instance-admin : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-app-instance-admin.html
	delete-app-instance-admin : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-app-instance-admin.html
	list-app-instance-admins : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-app-instance-admins.html
    """

    parameter_display_string = """
    # app-instance-admin-arn : The ARN of the app instance administrator.
    # app-instance-arn : The ARN of the app instance.
    """

    execute_two_parameter("chime", "describe-app-instance-admin", "app-instance-admin-arn", "app-instance-arn", parameter_display_string)