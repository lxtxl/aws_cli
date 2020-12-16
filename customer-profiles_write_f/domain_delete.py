#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/create-domain.html
	get-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/list-domains.html
	update-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/update-domain.html
    """

    write_parameter("customer-profiles", "delete-domain")