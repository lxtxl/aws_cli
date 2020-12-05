#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-v2-logging-level : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-v2-logging-level.html
	list-v2-logging-levels : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-v2-logging-levels.html
    """

    write_parameter("iot", "set-v2-logging-level")