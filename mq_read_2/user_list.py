#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/describe-user.html
if __name__ == '__main__':
    """
	create-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-user.html
	delete-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/delete-user.html
	list-users : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/list-users.html
	update-user : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/update-user.html
    """

    parameter_display_string = """
    # broker-id : The unique ID that Amazon MQ generates for the broker.
    # username : The username of the ActiveMQ user. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 2-100 characters long.
    """

    execute_two_parameter("mq", "describe-user", "broker-id", "username", parameter_display_string)