#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/delete-cost-category-definition.html
	describe-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/describe-cost-category-definition.html
	list-cost-category-definitions : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-cost-category-definitions.html
	update-cost-category-definition : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/update-cost-category-definition.html
    """

    write_parameter("ce", "create-cost-category-definition")