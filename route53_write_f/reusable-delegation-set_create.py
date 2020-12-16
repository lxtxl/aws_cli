#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	delete-reusable-delegation-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-reusable-delegation-set.html
	get-reusable-delegation-set : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-reusable-delegation-set.html
	list-reusable-delegation-sets : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-reusable-delegation-sets.html
    """

    write_parameter("route53", "create-reusable-delegation-set")