#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-assessment-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/create-assessment-template.html
	describe-assessment-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-templates.html
	list-assessment-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/list-assessment-templates.html
    """

    write_parameter("inspector", "delete-assessment-template")