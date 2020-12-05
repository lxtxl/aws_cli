#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-project-version.html
	delete-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/delete-project-version.html
	describe-project-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/describe-project-versions.html
	start-project-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/start-project-version.html
    """

    write_parameter("rekognition", "stop-project-version")