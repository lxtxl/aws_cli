#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/list-requested-service-quota-change-history-by-quota.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # service-code : Specifies the service that you want to use.
    # quota-code : Specifies the service quota that you want to use
    """

    execute_two_parameter("service-quotas", "list-requested-service-quota-change-history-by-quota", "service-code", "quota-code", parameter_display_string)