#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/create-queue.html
	get-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-queue.html
	list-queues : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-queues.html
	update-queue : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/update-queue.html
    """

    write_parameter("mediaconvert", "delete-queue")