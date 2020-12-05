#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-report-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/create-report-group.html
	list-report-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/list-report-groups.html
	update-report-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-report-group.html
    """

    write_parameter("codebuild", "delete-report-group")