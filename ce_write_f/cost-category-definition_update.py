#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/create-cost-category-definition.html
	delete-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/delete-cost-category-definition.html
	describe-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/describe-cost-category-definition.html
	list-cost-category-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-cost-category-definitions.html
    """

    write_parameter("ce", "update-cost-category-definition")