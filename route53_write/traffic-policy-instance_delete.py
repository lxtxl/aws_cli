#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-traffic-policy-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-traffic-policy-instance.html
	get-traffic-policy-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-traffic-policy-instance.html
	list-traffic-policy-instances : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-traffic-policy-instances.html
	update-traffic-policy-instance : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/update-traffic-policy-instance.html
    """

    write_parameter("route53", "delete-traffic-policy-instance")