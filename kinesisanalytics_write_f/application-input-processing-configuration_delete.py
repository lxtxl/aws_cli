#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	add-application-input-processing-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalytics/add-application-input-processing-configuration.html
    """

    write_parameter("kinesisanalytics", "delete-application-input-processing-configuration")