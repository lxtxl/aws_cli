#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mobile/create-project.html
	delete-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mobile/delete-project.html
	describe-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mobile/describe-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mobile/list-projects.html
	update-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mobile/update-project.html
    """

    write_parameter("mobile", "export-project")