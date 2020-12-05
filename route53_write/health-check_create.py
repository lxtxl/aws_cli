#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-health-check.html
	get-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-health-check.html
	list-health-checks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-health-checks.html
	update-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/update-health-check.html
    """

    write_parameter("route53", "create-health-check")