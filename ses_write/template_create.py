#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/delete-template.html
	get-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/get-template.html
	list-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/list-templates.html
	update-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/update-template.html
    """

    write_parameter("ses", "create-template")