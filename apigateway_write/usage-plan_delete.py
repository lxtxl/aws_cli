#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-usage-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/create-usage-plan.html
	get-usage-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plan.html
	get-usage-plans : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/get-usage-plans.html
	update-usage-plan : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apigateway/update-usage-plan.html
    """

    write_parameter("apigateway", "delete-usage-plan")