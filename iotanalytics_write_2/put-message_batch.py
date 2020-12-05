#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotanalytics/batch-put-message.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # channel-name : The name of the channel where the messages are sent.
    # messages : The list of messages to be sent. Each message has the format: { âmessageIdâ: âstringâ, âpayloadâ: âstringâ}.
The field names of message payloads (data) that you send to AWS IoT Analytics:

Must contain only alphanumeric characters and undescores (_). No other special characters are allowed.
Must begin with an alphabetic character or single underscore (_).
Cannot contain hyphens (-).
In regular expression terms: â^[A-Za-z_]([A-Za-z0-9]*|[A-Za-z0-9][A-Za-z0-9_]*)$â.
Cannot be more than 255 characters.
Are case insensitive. (Fields named foo and FOO in the same payload are considered duplicates.)

For example, {âtemp_01â: 29} or {â_temp_01â: 29} are valid, but {âtemp-01â: 29}, {â01_tempâ: 29} or {â__temp_01â: 29} are invalid in message payloads.
(structure)

Information about a message.
messageId -> (string)

The ID you want to assign to the message. Each messageId must be unique within each batch sent.

payload -> (blob)

The payload of the message. This can be a JSON string or a base64-encoded string representing binary data, in which case you must decode it by means of a pipeline activity.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("iotanalytics", "batch-put-message", "channel-name", "messages", add_option_dict)
