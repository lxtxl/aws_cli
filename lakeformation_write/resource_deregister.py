#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/describe-resource.html
	list-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-resources.html
	register-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/register-resource.html
	update-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/update-resource.html
    """

    write_parameter("lakeformation", "deregister-resource")