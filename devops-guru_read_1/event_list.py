#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_one_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/devops-guru/list-events.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # filters : Used to select a set of devices. A filter is made up of an attribute, an operator, and one or more values.

Attribute: The aspect of a device such as platform or model used as the selection criteria in a device filter. Allowed values include:

ARN: The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example ).
PLATFORM: The device platform. Valid values are ANDROID or IOS.
OS_VERSION: The operating system version (for example, 10.3.2).
MODEL: The device model (for example, iPad 5th Gen).
AVAILABILITY: The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
FORM_FACTOR: The device form factor. Valid values are PHONE or TABLET.
MANUFACTURER: The device manufacturer (for example, Apple).
REMOTE_ACCESS_ENABLED: Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
REMOTE_DEBUG_ENABLED: Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE. Because remote debugging is no longer supported , this attribute is ignored.
INSTANCE_ARN: The Amazon Resource Name (ARN) of the device instance.
INSTANCE_LABELS: The label of the device instance.
FLEET_TYPE: The fleet type. Valid values are PUBLIC or PRIVATE.


Operator: The filter operator.

The EQUALS operator is available for every attribute except INSTANCE_LABELS.
The CONTAINS operator is available for the INSTANCE_LABELS and MODEL attributes.
The IN and NOT_IN operators are available for the ARN, OS_VERSION, MODEL, MANUFACTURER, and INSTANCE_ARN attributes.
The LESS_THAN, GREATER_THAN, LESS_THAN_OR_EQUALS, and GREATER_THAN_OR_EQUALS operators are also available for the OS_VERSION attribute.


Values: An array of one or more filter values.

The IN and NOT_IN operators take a values array that has one or more elements.
The other operators require an array with a single element.
In a request, the AVAILABILITY attribute takes the following values: AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.



(structure)

Represents a device filter used to select a set of devices to be included in a test run. This data structure is passed in as the deviceSelectionConfiguration parameter to ScheduleRun . For an example of the JSON request syntax, see  ScheduleRun .
It is also passed in as the filters parameter to ListDevices . For an example of the JSON request syntax, see  ListDevices .
attribute -> (string)

The aspect of a device such as platform or model used as the selection criteria in a device filter.
The supported operators for each attribute are provided in the following list.

ARN

The Amazon Resource Name (ARN) of the device (for example, arn:aws:devicefarm:us-west-2::device:12345Example ).
Supported operators: EQUALS , IN , NOT_IN

PLATFORM

The device platform. Valid values are ANDROID or IOS.
Supported operators: EQUALS

OS_VERSION

The operating system version (for example, 10.3.2).
Supported operators: EQUALS , GREATER_THAN , GREATER_THAN_OR_EQUALS , IN , LESS_THAN , LESS_THAN_OR_EQUALS , NOT_IN

MODEL

The device model (for example, iPad 5th Gen).
Supported operators: CONTAINS , EQUALS , IN , NOT_IN

AVAILABILITY

The current availability of the device. Valid values are AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
Supported operators: EQUALS

FORM_FACTOR

The device form factor. Valid values are PHONE or TABLET.
Supported operators: EQUALS

MANUFACTURER

The device manufacturer (for example, Apple).
Supported operators: EQUALS , IN , NOT_IN

REMOTE_ACCESS_ENABLED

Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
Supported operators: EQUALS

REMOTE_DEBUG_ENABLED

Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE.
Supported operators: EQUALS
Because remote debugging is no longer supported , this filter is ignored.

INSTANCE_ARN

The Amazon Resource Name (ARN) of the device instance.
Supported operators: EQUALS , IN , NOT_IN

INSTANCE_LABELS

The label of the device instance.
Supported operators: CONTAINS

FLEET_TYPE

The fleet type. Valid values are PUBLIC or PRIVATE.
Supported operators: EQUALS

operator -> (string)

Specifies how Device Farm compares the filterâs attribute to the value. See the attribute descriptions.

values -> (list)

An array of one or more filter values used in a device filter.

Operator Values


The IN and NOT_IN operators can take a values array that has more than one element.
The other operators require an array with a single element.


Attribute Values


The PLATFORM attribute can be set to ANDROID or IOS.
The AVAILABILITY attribute can be set to AVAILABLE, HIGHLY_AVAILABLE, BUSY, or TEMPORARY_NOT_AVAILABLE.
The FORM_FACTOR attribute can be set to PHONE or TABLET.
The FLEET_TYPE attribute can be set to PUBLIC or PRIVATE.

(string)
    """

    add_option_dict = {}
    #######################################################################
    # setting option use
    # ex: add_option_dict["setting_matching_parameter"] = "--owners"
    # ex: add_option_dict["setting_key"] = "owner_id"

    #######################################################################
    # single parameter
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string

    execute_one_parameter("devops-guru", "list-events", "filters", add_option_dict)