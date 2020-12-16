#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-anomaly-detectors : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/describe-anomaly-detectors.html
	put-anomaly-detector : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudwatch/put-anomaly-detector.html
    """

    write_parameter("cloudwatch", "delete-anomaly-detector")