#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-hosted-zone : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-hosted-zone.html
	get-hosted-zone : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-hosted-zone.html
	list-hosted-zones : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-hosted-zones.html
    """

    write_parameter("route53", "create-hosted-zone")