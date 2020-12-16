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
	delete-theme : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-theme.html
	describe-theme : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-theme.html
	list-themes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-themes.html
    """

    write_parameter("quicksight", "update-theme")