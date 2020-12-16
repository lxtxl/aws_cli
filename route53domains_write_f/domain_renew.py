#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/list-domains.html
	register-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/register-domain.html
	transfer-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53domains/transfer-domain.html
    """

    write_parameter("route53domains", "renew-domain")