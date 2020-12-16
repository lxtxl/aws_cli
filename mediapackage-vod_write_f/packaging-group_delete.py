#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-packaging-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/create-packaging-group.html
	describe-packaging-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/describe-packaging-group.html
	list-packaging-groups : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/list-packaging-groups.html
	update-packaging-group : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/update-packaging-group.html
    """

    write_parameter("mediapackage-vod", "delete-packaging-group")