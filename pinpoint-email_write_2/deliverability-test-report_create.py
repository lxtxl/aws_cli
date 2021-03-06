#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/create-deliverability-test-report.html
if __name__ == '__main__':
    """
	get-deliverability-test-report : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-deliverability-test-report.html
	list-deliverability-test-reports : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/list-deliverability-test-reports.html
    """

    parameter_display_string = """
    # from-email-address : The email address that the predictive inbox placement test email was sent from.
    # content : If provided, the new content for the policy. The text must be correctly formatted JSON that complies with the syntax for the policyâs type. For more information, see Service Control Policy Syntax in the AWS Organizations User Guide.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("pinpoint-email", "create-deliverability-test-report", "from-email-address", "content", add_option_dict)
