#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-realtime-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/create-realtime-log-config.html
	get-realtime-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/get-realtime-log-config.html
	list-realtime-log-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/list-realtime-log-configs.html
	update-realtime-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudfront/update-realtime-log-config.html
    """

    write_parameter("cloudfront", "delete-realtime-log-config")