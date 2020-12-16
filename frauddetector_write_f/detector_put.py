#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/delete-detector.html
	describe-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/describe-detector.html
	get-detectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/frauddetector/get-detectors.html
    """

    write_parameter("frauddetector", "put-detector")