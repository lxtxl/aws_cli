#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-domain-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-domain-configuration.html
	delete-domain-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-domain-configuration.html
	describe-domain-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/describe-domain-configuration.html
	list-domain-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-domain-configurations.html
    """

    write_parameter("iot", "update-domain-configuration")