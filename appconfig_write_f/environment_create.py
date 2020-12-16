#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/delete-environment.html
	get-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-environment.html
	list-environments : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-environments.html
	update-environment : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/update-environment.html
    """

    write_parameter("appconfig", "create-environment")