#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-health-check.html
if __name__ == '__main__':
    """
	delete-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/delete-health-check.html
	get-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-health-check.html
	list-health-checks : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/list-health-checks.html
	update-health-check : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/update-health-check.html
    """

    parameter_display_string = """
    # caller-reference : A unique string that identifies the request and that allows you to retry a failed CreateHealthCheck request without the risk of creating two identical health checks:

If you send a CreateHealthCheck request with the same CallerReference and settings as a previous request, and if the health check doesnât exist, Amazon Route 53 creates the health check. If the health check does exist, Route 53 returns the settings for the existing health check.
If you send a CreateHealthCheck request with the same CallerReference as a deleted health check, regardless of the settings, Route 53 returns a HealthCheckAlreadyExists error.
If you send a CreateHealthCheck request with the same CallerReference as an existing health check but with different settings, Route 53 returns a HealthCheckAlreadyExists error.
If you send a CreateHealthCheck request with a unique CallerReference but settings identical to an existing health check, Route 53 creates the health check.
    # health-check-config : 
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53", "create-health-check", "caller-reference", "health-check-config", add_option_dict)
