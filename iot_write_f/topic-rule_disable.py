#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-topic-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-topic-rule.html
	delete-topic-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/delete-topic-rule.html
	enable-topic-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/enable-topic-rule.html
	get-topic-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-topic-rule.html
	list-topic-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-topic-rules.html
	replace-topic-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/replace-topic-rule.html
    """

    write_parameter("iot", "disable-topic-rule")