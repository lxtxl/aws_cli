#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-scheduled-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/create-scheduled-action.html
	describe-scheduled-actions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/describe-scheduled-actions.html
	modify-scheduled-action : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/modify-scheduled-action.html
    """

    write_parameter("redshift", "delete-scheduled-action")