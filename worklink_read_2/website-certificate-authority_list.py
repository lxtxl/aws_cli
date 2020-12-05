#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/describe-website-certificate-authority.html
if __name__ == '__main__':
    """
	associate-website-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/associate-website-certificate-authority.html
	disassociate-website-certificate-authority : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/disassociate-website-certificate-authority.html
	list-website-certificate-authorities : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-website-certificate-authorities.html
    """

    parameter_display_string = """
    # fleet-arn : The ARN of the fleet.
    # website-ca-id : A unique identifier for the certificate authority.
    """

    execute_two_parameter("worklink", "describe-website-certificate-authority", "fleet-arn", "website-ca-id", parameter_display_string)