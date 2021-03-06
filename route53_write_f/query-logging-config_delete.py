#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-query-logging-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-query-logging-config.html
	get-query-logging-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-query-logging-config.html
	list-query-logging-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-query-logging-configs.html
    """

    write_parameter("route53", "delete-query-logging-config")