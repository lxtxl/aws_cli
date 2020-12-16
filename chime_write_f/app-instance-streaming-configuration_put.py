#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-app-instance-streaming-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-app-instance-streaming-configurations.html
	get-app-instance-streaming-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-app-instance-streaming-configurations.html
    """

    write_parameter("chime", "put-app-instance-streaming-configurations")