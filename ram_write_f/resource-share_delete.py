#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/associate-resource-share.html
	create-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/create-resource-share.html
	disassociate-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/disassociate-resource-share.html
	get-resource-shares : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/get-resource-shares.html
	update-resource-share : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ram/update-resource-share.html
    """

    write_parameter("ram", "delete-resource-share")