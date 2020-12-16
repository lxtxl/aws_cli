#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/delete-config.html
	get-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/get-config.html
	list-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/list-configs.html
	update-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/update-config.html
    """

    write_parameter("groundstation", "create-config")