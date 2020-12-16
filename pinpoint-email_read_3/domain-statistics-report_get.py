#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-domain-statistics-report.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # domain : The domain that you want to obtain deliverability metrics for.
    # start-date : 
    """

    execute_two_parameter("pinpoint-email", "get-domain-statistics-report", "domain", "start-date", parameter_display_string)