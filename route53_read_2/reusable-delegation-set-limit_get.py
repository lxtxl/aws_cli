#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-reusable-delegation-set-limit.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # type : Specify MAX_ZONES_BY_REUSABLE_DELEGATION_SET to get the maximum number of hosted zones that you can associate with the specified reusable delegation set.
Possible values:

MAX_ZONES_BY_REUSABLE_DELEGATION_SET
    # delegation-set-id : The ID of the delegation set that you want to get the limit for.
    """

    execute_two_parameter("route53", "get-reusable-delegation-set-limit", "type", "delegation-set-id", parameter_display_string)