#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/create-delivery-stream.html
	delete-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/delete-delivery-stream.html
	describe-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/describe-delivery-stream.html
	list-delivery-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/list-delivery-streams.html
	untag-delivery-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/untag-delivery-stream.html
    """

    write_parameter("firehose", "tag-delivery-stream")