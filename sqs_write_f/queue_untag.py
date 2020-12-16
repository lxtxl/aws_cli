#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/create-queue.html
	delete-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/delete-queue.html
	list-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/list-queues.html
	purge-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/purge-queue.html
	tag-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/tag-queue.html
    """

    write_parameter("sqs", "untag-queue")