#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/delete-project.html
	describe-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/describe-project.html
	list-projects : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/list-projects.html
	tag-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/tag-project.html
	untag-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/untag-project.html
	update-project : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codestar/update-project.html
    """

    write_parameter("codestar", "create-project")