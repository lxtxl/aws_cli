#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	deregister-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/deregister-resource.html
	describe-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/describe-resource.html
	list-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-resources.html
	register-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/register-resource.html
    """

    write_parameter("lakeformation", "update-resource")