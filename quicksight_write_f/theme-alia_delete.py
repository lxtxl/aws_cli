#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-theme-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-theme-alias.html
	describe-theme-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-theme-alias.html
	update-theme-alias : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/update-theme-alias.html
    """

    write_parameter("quicksight", "delete-theme-alias")