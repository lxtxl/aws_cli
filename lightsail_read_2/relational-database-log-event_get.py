#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-log-events.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # relational-database-name : The name of your database for which to get log events.
    # log-stream-name : The name of the log stream.
Use the get relational database log streams operation to get a list of available log streams.
    """

    execute_two_parameter("lightsail", "get-relational-database-log-events", "relational-database-name", "log-stream-name", parameter_display_string)