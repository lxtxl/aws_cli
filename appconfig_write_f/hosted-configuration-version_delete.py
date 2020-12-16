#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-hosted-configuration-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/create-hosted-configuration-version.html
	get-hosted-configuration-version : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/get-hosted-configuration-version.html
	list-hosted-configuration-versions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appconfig/list-hosted-configuration-versions.html
    """

    write_parameter("appconfig", "delete-hosted-configuration-version")