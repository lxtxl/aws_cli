#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-packaging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/delete-packaging-configuration.html
	describe-packaging-configuration : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/describe-packaging-configuration.html
	list-packaging-configurations : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/list-packaging-configurations.html
    """

    write_parameter("mediapackage-vod", "create-packaging-configuration")