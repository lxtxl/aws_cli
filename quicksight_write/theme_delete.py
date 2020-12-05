#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-theme : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-theme.html
	describe-theme : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-theme.html
	list-themes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-themes.html
	update-theme : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-theme.html
    """

    write_parameter("quicksight", "delete-theme")