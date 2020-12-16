#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/get-service-quota-increase-request-from-template.html
if __name__ == '__main__':
    """
	delete-service-quota-increase-request-from-template : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/delete-service-quota-increase-request-from-template.html
    """

    parameter_display_string = """
    # service-code : Specifies the service that you want to use.
    # quota-code : Specifies the quota you want.
    """

    execute_two_parameter("service-quotas", "get-service-quota-increase-request-from-template", "service-code", "quota-code", parameter_display_string)