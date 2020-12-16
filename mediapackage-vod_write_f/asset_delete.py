#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/create-asset.html
	describe-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/describe-asset.html
	list-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackage-vod/list-assets.html
    """

    write_parameter("mediapackage-vod", "delete-asset")