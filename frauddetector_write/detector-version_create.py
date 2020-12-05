#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-detector-version.html
	get-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-detector-version.html
	update-detector-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/update-detector-version.html
    """

    write_parameter("frauddetector", "create-detector-version")