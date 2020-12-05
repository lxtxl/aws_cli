#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	associate-website-authorization-provider : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/associate-website-authorization-provider.html
	list-website-authorization-providers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-website-authorization-providers.html
    """

    write_parameter("worklink", "disassociate-website-authorization-provider")