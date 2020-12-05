#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-query-logging-config.html
if __name__ == '__main__':
    """
	delete-query-logging-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-query-logging-config.html
	get-query-logging-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-query-logging-config.html
	list-query-logging-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-query-logging-configs.html
    """

    parameter_display_string = """
    # hosted-zone-id : The ID of the hosted zone that you want to log queries for. You can log queries only for public hosted zones.
    # cloud-watch-logs-log-group-arn : The Amazon Resource Name (ARN) for the log group that you want to Amazon Route 53 to send query logs to. This is the format of the ARN:
arn:aws:logs:region :account-id :log-group:log_group_name
To get the ARN for a log group, you can use the CloudWatch console, the DescribeLogGroups API action, the describe-log-groups command, or the applicable command in one of the AWS SDKs.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53", "create-query-logging-config", "hosted-zone-id", "cloud-watch-logs-log-group-arn", add_option_dict)
