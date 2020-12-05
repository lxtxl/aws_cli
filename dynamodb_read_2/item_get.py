#!/usr/bin/python
# -*- codding: utf-8 -*-
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from common.execute_command import execute_two_parameter


# url : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/get-item.html
if __name__ == '__main__':
    """
	delete-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/delete-item.html
	put-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/put-item.html
	update-item : https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dynamodb/update-item.html
    """

    parameter_display_string = """
    # table-name : The name of the table containing the requested item.
    # key : A map of attribute names to AttributeValue objects, representing the primary key of the item to retrieve.
For the primary key, you must provide all of the attributes. For example, with a simple primary key, you only need to provide a value for the partition key. For a composite primary key, you must provide values for both the partition key and the sort key.
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
    """

    execute_two_parameter("dynamodb", "get-item", "table-name", "key", parameter_display_string)