#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-world-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/delete-world-template.html
	describe-world-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/describe-world-template.html
	list-world-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/list-world-templates.html
	update-world-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/update-world-template.html
    """

    write_parameter("robomaker", "create-world-template")