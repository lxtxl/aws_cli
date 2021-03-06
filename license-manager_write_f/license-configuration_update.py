#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-license-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/create-license-configuration.html
	delete-license-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/delete-license-configuration.html
	get-license-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/get-license-configuration.html
	list-license-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/license-manager/list-license-configurations.html
    """

    write_parameter("license-manager", "update-license-configuration")