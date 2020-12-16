#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-domain-deliverability-campaigns.html
if __name__ == '__main__':
    """
	get-domain-deliverability-campaign : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-domain-deliverability-campaign.html
    """

    parameter_display_string = """
    # start-date : 
    # end-date : 
    """

    execute_two_parameter("sesv2", "list-domain-deliverability-campaigns", "start-date", "end-date", parameter_display_string)