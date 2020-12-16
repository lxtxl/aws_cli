#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-iam-policy-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-iam-policy-assignment.html
	delete-iam-policy-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/delete-iam-policy-assignment.html
	describe-iam-policy-assignment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/describe-iam-policy-assignment.html
	list-iam-policy-assignments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/list-iam-policy-assignments.html
    """

    write_parameter("quicksight", "update-iam-policy-assignment")