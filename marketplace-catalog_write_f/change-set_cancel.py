#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/describe-change-set.html
	list-change-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/list-change-sets.html
	start-change-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/marketplace-catalog/start-change-set.html
    """

    write_parameter("marketplace-catalog", "cancel-change-set")