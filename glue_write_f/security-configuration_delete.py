#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-security-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/create-security-configuration.html
	get-security-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-security-configuration.html
	get-security-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-security-configurations.html
    """

    write_parameter("glue", "delete-security-configuration")