#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-phone-number : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/get-phone-number.html
	list-phone-numbers : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/list-phone-numbers.html
	restore-phone-number : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/restore-phone-number.html
	update-phone-number : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-phone-number.html
    """

    write_parameter("chime", "delete-phone-number")