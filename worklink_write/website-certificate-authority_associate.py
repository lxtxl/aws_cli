#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	describe-website-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/describe-website-certificate-authority.html
	disassociate-website-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/disassociate-website-certificate-authority.html
	list-website-certificate-authorities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-website-certificate-authorities.html
    """

    write_parameter("worklink", "associate-website-certificate-authority")