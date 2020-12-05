#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/create-project.html
	describe-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/list-projects.html
	update-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/update-project.html
    """

    write_parameter("databrew", "delete-project")