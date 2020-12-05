#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-logging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/delete-logging-configuration.html
	get-logging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/get-logging-configuration.html
	list-logging-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/list-logging-configurations.html
    """

    write_parameter("waf", "put-logging-configuration")