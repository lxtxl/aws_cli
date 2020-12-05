#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_two_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/batch-meter-usage.html
if __name__ == '__main__':
    """

    """

    parameter_display_string = """
    # usage-records : The set of UsageRecords to submit. BatchMeterUsage accepts up to 25 UsageRecords at a time.
(structure)

A UsageRecord indicates a quantity of usage for a given product, customer, dimension and time.
Multiple requests with the same UsageRecords as input will be deduplicated to prevent double charges.
Timestamp -> (timestamp)

Timestamp, in UTC, for which the usage is being reported.
Your application can meter usage for up to one hour in the past. Make sure the timestamp value is not before the start of the software usage.

CustomerIdentifier -> (string)

The CustomerIdentifier is obtained through the ResolveCustomer operation and represents an individual buyer in your application.

Dimension -> (string)

During the process of registering a product on AWS Marketplace, up to eight dimensions are specified. These represent different units of value in your application.

Quantity -> (integer)

The quantity of usage consumed by the customer for the given dimension and time. Defaults to 0 if not specified.

UsageAllocations -> (list)

The set of UsageAllocations to submit. The sum of all UsageAllocation quantities must equal the Quantity of the UsageRecord.
(structure)

Usage allocations allow you to split usage into buckets by tags.
Each UsageAllocation indicates the usage quantity for a specific set of tags.
AllocatedUsageQuantity -> (integer)

The total quantity allocated to this bucket of usage.

Tags -> (list)

The set of tags that define the bucket of usage. For the bucket of items with no tags, this parameter can be left out.
(structure)

Metadata assigned to an allocation. Each tag is made up of a key and a value.
Key -> (string)

One part of a key-value pair that makes up a tag. A key is a label that acts like a category for the specific tag values.

Value -> (string)

One part of a key-value pair that makes up a tag. A value acts as a descriptor within a tag category (key). The value can be empty or null.
    # product-code : Product code is used to uniquely identify a product in AWS Marketplace. The product code should be the same as the one used during the publishing of a new product.
    """
    add_option_dict = {}
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_two_parameter("meteringmarketplace", "batch-meter-usage", "usage-records", "product-code", add_option_dict)
