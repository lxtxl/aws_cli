#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_three_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/create-device-pool.html
if __name__ == '__main__':
    """
	delete-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/delete-device-pool.html
	get-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/get-device-pool.html
	list-device-pools : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/list-device-pools.html
	update-device-pool : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devicefarm/update-device-pool.html
    """

    parameter_display_string = """
    # project-arn : The ARN of the project for the device pool.
    # name : The device poolâs name.
    # rules : The device poolâs rules.
(structure)

Represents a condition for a device pool.
attribute -> (string)

The ruleâs stringified attribute. For example, specify the value as "\"abc\"" .
The supported operators for each attribute are provided in the following list.

APPIUM_VERSION

The Appium version for the test.
Supported operators: CONTAINS

ARN

The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example .
Supported operators: EQUALS , IN , NOT_IN

AVAILABILITY

The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
Supported operators: EQUALS

FLEET_TYPE

The fleet type. Valid values are PUBLIC or PRIVATE.
Supported operators: EQUALS

FORM_FACTOR

The device form factor. Valid values are PHONE or TABLET.
Supported operators: EQUALS , IN , NOT_IN

INSTANCE_ARN

The Amazon Resource Name (ARN) of the device instance.
Supported operators: IN , NOT_IN

INSTANCE_LABELS

The label of the device instance.
Supported operators: CONTAINS

MANUFACTURER

The device manufacturer (for example, Apple).
Supported operators: EQUALS , IN , NOT_IN

MODEL

The device model, such as Apple iPad Air 2 or Google Pixel.
Supported operators: CONTAINS , EQUALS , IN , NOT_IN

OS_VERSION

The operating system version (for example, 10.3.2).
Supported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN

PLATFORM

The device platform. Valid values are ANDROID or IOS.
Supported operators: EQUALS , IN , NOT_IN

REMOTE_ACCESS_ENABLED

Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
Supported operators: EQUALS

REMOTE_DEBUG_ENABLED

Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.
Supported operators: EQUALS
Because remote debugging is no longer supported , this filter is ignored.

operator -> (string)

Specifies how Device Farm compares the ruleâs attribute to the value. For the operators that are supported by each attribute, see the attribute descriptions.

value -> (string)

The ruleâs value.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_three_parameter("devicefarm", "create-device-pool", "project-arn", "name", "rules", add_option_dict)
