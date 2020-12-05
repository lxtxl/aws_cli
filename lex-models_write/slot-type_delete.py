#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	get-slot-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-slot-type.html
	get-slot-types : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/get-slot-types.html
	put-slot-type : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lex-models/put-slot-type.html
    """

    write_parameter("lex-models", "delete-slot-type")