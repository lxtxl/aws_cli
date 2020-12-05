#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/associate-assets.html
	create-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/create-asset.html
	describe-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset.html
	disassociate-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/disassociate-assets.html
	list-assets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-assets.html
	update-asset : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-asset.html
    """

    write_parameter("iotsitewise", "delete-asset")