# Customer Data System

A Python-based customer data management system that demonstrates core CRM functionality.

## Overview

This project focuses on managing and structuring customer data and interactions.

The system supports:
- adding customers with contact details (email and phone)
- updating customer information
- logging customer interactions
- tracking time since the last interaction
- basic error handling for invalid operations

## Why this project

This project demonstrates how structured customer data can be handled in a simple system.

It reflects core concepts used in CRM systems, such as:
- data organization and state management
- tracking interactions over time
- validating and updating customer records
- handling missing or incorrect data

## Skills demonstrated

- Python programming
- Object-oriented design
- Data structures and state management
- Basic system design
- Error handling and validation
- Writing clear and structured program logic

## How it works

- Customers are stored in a collection within the system
- Each customer has contact information and a list of interactions
- Interactions update the customer's latest activity timestamp
- The system can calculate time since last interaction
- Invalid operations raise errors (e.g. missing customer)

## Project structure

- `main.py` — contains the core system logic and example usage
- 
## Example usage

```python
system = CustomerDataSystem("CRM Demo")

system.add_customer("Customer A", "a@example.com", "0700000000")
system.add_customer_interaction("Customer A", "Initial contact")

customer = system.get_customer("Customer A")
days = customer.days_since_last_interaction()
```

## Notes

- This is an educational project focused on core logic and structure
- Demo data is anonymized using placeholders
- The system runs in-memory (no database)

## Author

Built as part of a programming and data systems learning process.
