#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/create-sip-rule.html
	delete-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/delete-sip-rule.html
	get-sip-rule : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-sip-rule.html
	list-sip-rules : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-sip-rules.html
    """

    write_parameter("chime", "update-sip-rule")