#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/create-stream.html
	delete-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/delete-stream.html
	describe-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/describe-stream.html
	list-streams : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/list-streams.html
	tag-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/tag-stream.html
	untag-stream : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisvideo/untag-stream.html
    """

    write_parameter("kinesisvideo", "update-stream")