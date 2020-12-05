#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/describe-update.html
if __name__ == '__main__':
    """
	list-updates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/eks/list-updates.html
    """

    parameter_display_string = """
    # name : The name of the Amazon EKS cluster associated with the update.
    # update-id : The ID of the update to describe.
    """

    execute_two_parameter("eks", "describe-update", "name", "update-id", parameter_display_string)