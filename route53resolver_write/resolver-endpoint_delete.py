#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-resolver-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-endpoint.html
	get-resolver-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-endpoint.html
	list-resolver-endpoints : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-endpoints.html
	update-resolver-endpoint : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/update-resolver-endpoint.html
    """

    write_parameter("route53resolver", "delete-resolver-endpoint")