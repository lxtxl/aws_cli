#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	list-tags-for-resource : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-tags-for-resource.html
	list-tags-for-resources : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-tags-for-resources.html
    """

    write_parameter("route53", "change-tags-for-resource")