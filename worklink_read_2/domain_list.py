#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/describe-domain.html
if __name__ == '__main__':
    """
	associate-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/associate-domain.html
	disassociate-domain : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/disassociate-domain.html
	list-domains : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/worklink/list-domains.html
    """

    parameter_display_string = """
    # fleet-arn : The ARN of the fleet.
    # domain-name : The name of the domain.
    """

    execute_two_parameter("worklink", "describe-domain", "fleet-arn", "domain-name", parameter_display_string)