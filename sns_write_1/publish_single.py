#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sns/publish.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # message : The message you want to send.
If you are publishing to a topic and you want to send the same message to all transport protocols, include the text of the message as a String value. If you want to send different messages for each transport protocol, set the value of the MessageStructure parameter to json and use a JSON object for the Message parameter.
Constraints:

With the exception of SMS, messages must be UTF-8 encoded strings and at most 256 KB in size (262,144 bytes, not 262,144 characters).
For SMS, each message can contain up to 140 characters. This character limit depends on the encoding schema. For example, an SMS message can contain 160 GSM characters, 140 ASCII characters, or 70 UCS-2 characters. If you publish a message that exceeds this size limit, Amazon SNS sends the message as multiple messages, each fitting within the size limit. Messages arenât truncated mid-word but are cut off at whole-word boundaries. The total size limit for a single SMS Publish action is 1,600 characters.

JSON-specific constraints:

Keys in the JSON object that correspond to supported transport protocols must have simple JSON string values.
The values will be parsed (unescaped) before they are used in outgoing messages.
Outbound notifications are JSON encoded (meaning that the characters will be reescaped for sending).
Values have a minimum length of 0 (the empty string, ââ, is allowed).
Values have a maximum length bounded by the overall message size (so, including multiple protocols may limit message sizes).
Non-string values will cause the key to be ignored.
Keys that do not correspond to supported transport protocols are ignored.
Duplicate keys are not allowed.
Failure to parse or validate any key or value in the message will cause the Publish call to return an error (no partial delivery).
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("sns", "publish", "message", add_option_dict)





