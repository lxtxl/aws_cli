#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-logging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-logging-configuration.html
	list-logging-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-logging-configurations.html
	put-logging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/put-logging-configuration.html
    """

    write_parameter("wafv2", "delete-logging-configuration")