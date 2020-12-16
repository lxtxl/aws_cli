#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-vpce-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-vpce-configuration.html
	delete-vpce-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-vpce-configuration.html
	get-vpce-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-vpce-configuration.html
	list-vpce-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-vpce-configurations.html
    """

    write_parameter("devicefarm", "update-vpce-configuration")