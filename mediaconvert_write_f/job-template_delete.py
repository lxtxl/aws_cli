#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-job-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-job-template.html
	get-job-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-job-template.html
	list-job-templates : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-job-templates.html
	update-job-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-job-template.html
    """

    write_parameter("mediaconvert", "delete-job-template")