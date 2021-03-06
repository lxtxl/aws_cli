#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/associate-domain.html
	describe-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/describe-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-domains.html
    """

    write_parameter("worklink", "disassociate-domain")