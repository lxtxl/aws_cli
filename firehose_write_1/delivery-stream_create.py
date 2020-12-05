#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/create-delivery-stream.html
if __name__ == '__main__':
    """
	delete-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/delete-delivery-stream.html
	describe-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/describe-delivery-stream.html
	list-delivery-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/list-delivery-streams.html
	tag-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/tag-delivery-stream.html
	untag-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/untag-delivery-stream.html
    """

    parameter_display_string = """
    # delivery-stream-name : The name of the delivery stream. This name must be unique per AWS account in the same AWS Region. If the delivery streams are in different accounts or different Regions, you can have multiple delivery streams with the same name.
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("firehose", "create-delivery-stream", "delivery-stream-name", add_option_dict)





