#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-app-validation-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/get-app-validation-configuration.html
	put-app-validation-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sms/put-app-validation-configuration.html
    """

    write_parameter("sms", "delete-app-validation-configuration")