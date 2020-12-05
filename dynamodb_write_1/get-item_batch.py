#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import write_one_parameter

# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/batch-get-item.html
if __name__ == '__main__':
    """
	transact-get-items : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/transact-get-items.html
    """

    parameter_display_string = """
    # request-items : A map of one or more table names and, for each table, a map that describes one or more items to retrieve from that table. Each table name can be used only once per BatchGetItem request.
Each element in the map of items to retrieve consists of the following:

ConsistentRead - If true , a strongly consistent read is used; if false (the default), an eventually consistent read is used.
ExpressionAttributeNames - One or more substitution tokens for attribute names in the ProjectionExpression parameter. The following are some use cases for using ExpressionAttributeNames :

To access an attribute whose name conflicts with a DynamoDB reserved word.
To create a placeholder for repeating occurrences of an attribute name in an expression.
To prevent special characters in an attribute name from being misinterpreted in an expression.



Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name:


Percentile


The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide ). To work around this, you could specify the following for ExpressionAttributeNames :


{"#P":"Percentile"}


You could then use this substitution in an expression, as in this example:


#P = :val



Note
Tokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.

For more information about expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide .

Keys - An array of primary key attribute values that define specific items in the table. For each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide the partition key value. For a composite key, you must provide both the partition key value and the sort key value.
ProjectionExpression - A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes are returned. If any of the requested attributes are not found, they do not appear in the result. For more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide .
AttributesToGet - This is a legacy parameter. Use ProjectionExpression instead. For more information, see AttributesToGet in the Amazon DynamoDB Developer Guide .

key -> (string)
value -> (structure)

Represents a set of primary keys and, for each key, the attributes to retrieve from the table.
For each primary key, you must provide all of the key attributes. For example, with a simple primary key, you only need to provide the partition key. For a composite primary key, you must provide both the partition key and the sort key.
Keys -> (list)

The primary key attribute values that define the items and the attributes associated with the items.
(map)

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
value -> (structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

(structure)

Represents the data for an attribute.
Each attribute value is described as a name-value pair. The name is the data type, and the value is the data itself.
For more information, see Data Types in the Amazon DynamoDB Developer Guide .
S -> (string)

An attribute of type String. For example:

"S": "Hello"


N -> (string)

An attribute of type Number. For example:

"N": "123.45"

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.

B -> (blob)

An attribute of type Binary. For example:

"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"


SS -> (list)

An attribute of type String Set. For example:

"SS": ["Giraffe", "Hippo" ,"Zebra"]

(string)

NS -> (list)

An attribute of type Number Set. For example:

"NS": ["42.2", "-19", "7.5", "3.14"]

Numbers are sent across the network to DynamoDB as strings, to maximize compatibility across languages and libraries. However, DynamoDB treats them as number type attributes for mathematical operations.
(string)

BS -> (list)

An attribute of type Binary Set. For example:

"BS": ["U3Vubnk=", "UmFpbnk=", "U25vd3k="]

(blob)

M -> (map)

An attribute of type Map. For example:

"M": {"Name": {"S": "Joe"}, "Age": {"N": "35"}}

key -> (string)
( â¦ recursive â¦ )

L -> (list)

An attribute of type List. For example:

"L": [ {"S": "Cookies"} , {"S": "Coffee"}, {"N", "3.14159"}]

( â¦ recursive â¦ )

NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true




NULL -> (boolean)

An attribute of type Null. For example:

"NULL": true


BOOL -> (boolean)

An attribute of type Boolean. For example:

"BOOL": true





AttributesToGet -> (list)

This is a legacy parameter. Use ProjectionExpression instead. For more information, see Legacy Conditional Parameters in the Amazon DynamoDB Developer Guide .
(string)

ConsistentRead -> (boolean)

The consistency of a read operation. If set to true , then a strongly consistent read is used; otherwise, an eventually consistent read is used.

ProjectionExpression -> (string)

A string that identifies one or more attributes to retrieve from the table. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the ProjectionExpression must be separated by commas.
If no attribute names are specified, then all attributes will be returned. If any of the requested attributes are not found, they will not appear in the result.
For more information, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide .

ExpressionAttributeNames -> (map)

One or more substitution tokens for attribute names in an expression. The following are some use cases for using ExpressionAttributeNames :

To access an attribute whose name conflicts with a DynamoDB reserved word.
To create a placeholder for repeating occurrences of an attribute name in an expression.
To prevent special characters in an attribute name from being misinterpreted in an expression.

Use the # character in an expression to dereference an attribute name. For example, consider the following attribute name:

Percentile

The name of this attribute conflicts with a reserved word, so it cannot be used directly in an expression. (For the complete list of reserved words, see Reserved Words in the Amazon DynamoDB Developer Guide ). To work around this, you could specify the following for ExpressionAttributeNames :

{"#P":"Percentile"}

You could then use this substitution in an expression, as in this example:

#P = :val


Note
Tokens that begin with the : character are expression attribute values , which are placeholders for the actual value at runtime.

For more information on expression attribute names, see Accessing Item Attributes in the Amazon DynamoDB Developer Guide .
key -> (string)
value -> (string)
    """
    add_option_dict = {}

    #######################################################################
    # parameter display string
    add_option_dict["parameter_display_string"] = parameter_display_string
    # ex: add_option_dict["no_value_parameter_list"] = "--single-parameter"
    write_one_parameter("dynamodb", "batch-get-item", "request-items", add_option_dict)





