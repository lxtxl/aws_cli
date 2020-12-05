#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-query-log-config.html
if __name__ == '__main__':
    """
	associate-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/associate-resolver-query-log-config.html
	delete-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/delete-resolver-query-log-config.html
	disassociate-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/disassociate-resolver-query-log-config.html
	get-resolver-query-log-config : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/get-resolver-query-log-config.html
	list-resolver-query-log-configs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-query-log-configs.html
    """

    parameter_display_string = """
    # name : The name that you want to give the query logging configuration
    # destination-arn : The ARN of the resource that you want Resolver to send query logs. You can send query logs to an S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream. Examples of valid values include the following:

S3 bucket :   arn:aws:s3:::examplebucket   You can optionally append a file prefix to the end of the ARN.  arn:aws:s3:::examplebucket/development/
CloudWatch Logs log group :   arn:aws:logs:us-west-1:123456789012:log-group:/mystack-testgroup-12ABC1AB12A1:*
Kinesis Data Firehose delivery stream :  arn:aws:kinesis:us-east-2:0123456789:stream/my_stream_name
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("route53resolver", "create-resolver-query-log-config", "name", "destination-arn", add_option_dict)
