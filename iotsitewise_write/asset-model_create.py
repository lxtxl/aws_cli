#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-asset-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/delete-asset-model.html
	describe-asset-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-model.html
	list-asset-models : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/list-asset-models.html
	update-asset-model : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/update-asset-model.html
    """

    write_parameter("iotsitewise", "create-asset-model")