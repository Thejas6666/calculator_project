# 🧪 Test Plan: Calculator Module

## Objective:
To validate the functionality of basic arithmetic operations: add, subtract, multiply, and divide.

## Scope:
- Unit testing only
- Functional correctness for valid and invalid input

## Test Cases:
| ID  | Function     | Input           | Expected Output       | Remarks              |
|-----|--------------|-----------------|------------------------|----------------------|
| TC1 | add          | 2, 3            | 5                      | Basic addition       |
| TC2 | subtract     | 10, 4           | 6                      | Basic subtraction    |
| TC3 | multiply     | 3, 7            | 21                     | Basic multiplication |
| TC4 | divide       | 10, 2           | 5                      | Basic division       |
| TC5 | divide       | 5, 0            | Exception (ValueError) | Division by zero     |

## Tools Used:
- Python 3
- unittest
