#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-resource-data-sync : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/create-resource-data-sync.html
	list-resource-data-sync : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-resource-data-sync.html
	update-resource-data-sync : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-resource-data-sync.html
    """

    write_parameter("ssm", "delete-resource-data-sync")