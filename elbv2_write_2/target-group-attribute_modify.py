#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-target-group-attributes.html
if __name__ == '__main__':
    """
	describe-target-group-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-target-group-attributes.html
    """

    parameter_display_string = """
    # target-group-arn : The Amazon Resource Name (ARN) of the target group.
    # attributes : The attributes.
(structure)

Information about a target group attribute.
Key -> (string)

The name of the attribute.
The following attribute is supported by all load balancers:

deregistration_delay.timeout_seconds - The amount of time, in seconds, for Elastic Load Balancing to wait before changing the state of a deregistering target from draining to unused . The range is 0-3600 seconds. The default value is 300 seconds. If the target is a Lambda function, this attribute is not supported.

The following attributes are supported by both Application Load Balancers and Network Load Balancers:

stickiness.enabled - Indicates whether sticky sessions are enabled. The value is true or false . The default is false .
stickiness.type - The type of sticky sessions. The possible values are lb_cookie for Application Load Balancers or source_ip for Network Load Balancers.

The following attributes are supported only if the load balancer is an Application Load Balancer and the target is an instance or an IP address:

load_balancing.algorithm.type - The load balancing algorithm determines how the load balancer selects targets when routing requests. The value is round_robin or least_outstanding_requests . The default is round_robin .
slow_start.duration_seconds - The time period, in seconds, during which a newly registered target receives an increasing share of the traffic to the target group. After this time period ends, the target receives its full share of traffic. The range is 30-900 seconds (15 minutes). The default is 0 seconds (disabled).
stickiness.lb_cookie.duration_seconds - The time period, in seconds, during which requests from a client should be routed to the same target. After this time period expires, the load balancer-generated cookie is considered stale. The range is 1 second to 1 week (604800 seconds). The default value is 1 day (86400 seconds).

The following attribute is supported only if the load balancer is an Application Load Balancer and the target is a Lambda function:

lambda.multi_value_headers.enabled - Indicates whether the request and response headers that are exchanged between the load balancer and the Lambda function include arrays of values or strings. The value is true or false . The default is false . If the value is false and the request contains a duplicate header field name or query parameter key, the load balancer uses the last value sent by the client.

The following attribute is supported only by Network Load Balancers:

proxy_protocol_v2.enabled - Indicates whether Proxy Protocol version 2 is enabled. The value is true or false . The default is false .


Value -> (string)

The value of the attribute.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elbv2", "modify-target-group-attributes", "target-group-arn", "attributes", add_option_dict)
