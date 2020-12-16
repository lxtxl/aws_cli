#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-instances.html
if __name__ == '__main__':
    """
	disassociate-lex-bot : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/disassociate-lex-bot.html
	list-lex-bots : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/list-lex-bots.html
    """

    write_parameter("connect", "associate-lex-bot")