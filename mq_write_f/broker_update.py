#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/create-broker.html
	delete-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/delete-broker.html
	describe-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/describe-broker.html
	list-brokers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/list-brokers.html
	reboot-broker : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/reboot-broker.html
    """

    write_parameter("mq", "update-broker")