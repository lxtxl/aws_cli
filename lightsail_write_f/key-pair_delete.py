#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	create-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-key-pair.html
	get-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-key-pair.html
	get-key-pairs : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-key-pairs.html
	import-key-pair : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/import-key-pair.html
    """

    write_parameter("lightsail", "delete-key-pair")