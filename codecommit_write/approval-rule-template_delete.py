#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-approval-rule-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-approval-rule-template.html
	get-approval-rule-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-approval-rule-template.html
	list-approval-rule-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-approval-rule-templates.html
    """

    write_parameter("codecommit", "delete-approval-rule-template")