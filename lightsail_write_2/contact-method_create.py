#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-contact-method.html
if __name__ == '__main__':
    """
	delete-contact-method : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/delete-contact-method.html
	get-contact-methods : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-contact-methods.html
    """

    parameter_display_string = """
    # protocol : The protocol of the contact method, such as Email or SMS (text messaging).
The SMS protocol is supported only in the following AWS Regions.

US East (N. Virginia) (us-east-1 )
US West (Oregon) (us-west-2 )
Europe (Ireland) (eu-west-1 )
Asia Pacific (Tokyo) (ap-northeast-1 )
Asia Pacific (Singapore) (ap-southeast-1 )
Asia Pacific (Sydney) (ap-southeast-2 )

For a list of countries/regions where SMS text messages can be sent, and the latest AWS Regions where SMS text messaging is supported, see Supported Regions and Countries in the Amazon SNS Developer Guide .
For more information about notifications in Amazon Lightsail, see Notifications in Amazon Lightsail .
Possible values:

Email
SMS
    # contact-endpoint : The destination of the contact method, such as an email address or a mobile phone number.
Use the E.164 format when specifying a mobile phone number. E.164 is a standard for the phone number structure used for international telecommunication. Phone numbers that follow this format can have a maximum of 15 digits, and they are prefixed with the plus character (+) and the country code. For example, a U.S. phone number in E.164 format would be specified as +1XXX5550100. For more information, see E.164 on Wikipedia .
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("lightsail", "create-contact-method", "protocol", "contact-endpoint", add_option_dict)
