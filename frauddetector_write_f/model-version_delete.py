#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/create-model-version.html
	describe-model-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/describe-model-versions.html
	get-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-model-version.html
	update-model-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-model-version.html
    """

    write_parameter("frauddetector", "delete-model-version")