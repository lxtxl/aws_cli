#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/modify-load-balancer-attributes.html
if __name__ == '__main__':
    """
	describe-load-balancer-attributes : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-load-balancer-attributes.html
    """

    parameter_display_string = """
    # load-balancer-arn : The Amazon Resource Name (ARN) of the load balancer.
    # attributes : The load balancer attributes.
(structure)

Information about a load balancer attribute.
Key -> (string)

The name of the attribute.
The following attribute is supported by all load balancers:

deletion_protection.enabled - Indicates whether deletion protection is enabled. The value is true or false . The default is false .

The following attributes are supported by both Application Load Balancers and Network Load Balancers:

access_logs.s3.enabled - Indicates whether access logs are enabled. The value is true or false . The default is false .
access_logs.s3.bucket - The name of the S3 bucket for the access logs. This attribute is required if access logs are enabled. The bucket must exist in the same region as the load balancer and have a bucket policy that grants Elastic Load Balancing permissions to write to the bucket.
access_logs.s3.prefix - The prefix for the location in the S3 bucket for the access logs.

The following attributes are supported by only Application Load Balancers:

idle_timeout.timeout_seconds - The idle timeout value, in seconds. The valid range is 1-4000 seconds. The default is 60 seconds.
routing.http.desync_mitigation_mode - Determines how the load balancer handles requests that might pose a security risk to your application. The possible values are monitor , defensive , and strictest . The default is defensive .
routing.http.drop_invalid_header_fields.enabled - Indicates whether HTTP headers with invalid header fields are removed by the load balancer (true ) or routed to targets (false ). The default is false .
routing.http2.enabled - Indicates whether HTTP/2 is enabled. The value is true or false . The default is true . Elastic Load Balancing requires that message header names contain only alphanumeric characters and hyphens.

The following attribute is supported by Network Load Balancers and Gateway Load Balancers:

load_balancing.cross_zone.enabled - Indicates whether cross-zone load balancing is enabled. The value is true or false . The default is false .


Value -> (string)

The value of the attribute.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("elbv2", "modify-load-balancer-attributes", "load-balancer-arn", "attributes", add_option_dict)
