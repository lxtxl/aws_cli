#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/describe-user-hierarchy-group.html
if __name__ == '__main__':
    """
	list-user-hierarchy-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-user-hierarchy-groups.html
    """

    parameter_display_string = """
    # hierarchy-group-id : The identifier of the hierarchy group.
    # instance-id : The identifier of the Amazon Connect instance.
    """

    execute_two_parameter("connect", "describe-user-hierarchy-group", "hierarchy-group-id", "instance-id", parameter_display_string)