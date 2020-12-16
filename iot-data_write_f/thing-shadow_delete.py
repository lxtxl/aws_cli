#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-thing-shadow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/get-thing-shadow.html
	update-thing-shadow : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/update-thing-shadow.html
    """

    write_parameter("iot-data", "delete-thing-shadow")