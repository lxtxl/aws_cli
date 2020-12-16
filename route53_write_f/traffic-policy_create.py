#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-traffic-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-traffic-policy.html
	get-traffic-policy : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-traffic-policy.html
	list-traffic-policies : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policies.html
    """

    write_parameter("route53", "create-traffic-policy")