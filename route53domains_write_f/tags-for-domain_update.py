#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-tags-for-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/delete-tags-for-domain.html
	list-tags-for-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/list-tags-for-domain.html
    """

    write_parameter("route53domains", "update-tags-for-domain")