"""Customer Data System educational demo (anonymized data)."""

from datetime import datetime
from typing import Optional


class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.interactions = []
        self.last_interaction = None

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone}"

    def add_interaction(self, interaction):
        self.interactions.append(interaction)
        self.last_interaction = datetime.now()

    def days_since_last_interaction(self) -> Optional[int]:
        if self.last_interaction is None:
            return None
        return (datetime.now() - self.last_interaction).days


class CustomerDataSystem:
    def __init__(self, name: str):
        self.name = name
        self.customers = []

    def add_customer(self, name, email, phone):
        for customer in self.customers:
            if customer.email.lower() == email.lower():
                raise ValueError(f"A customer with email address {email} is already registered.")

        customer = Customer(name, email, phone)
        self.customers.append(customer)
        return customer

    def remove_customer(self, name):
        customer = self.get_customer(name)
        if customer is None:
            raise KeyError(f"Customer named {name} is not registered.")

        self.customers.remove(customer)
        return customer

    def update_customer_contact(self, name, email=None, phone=None):
        customer = self.get_customer(name)
        if customer is None:
            raise KeyError(f"Customer named {name} is not registered.")

        if email is not None:
            customer.email = email

        if phone is not None:
            customer.phone = phone

        return customer

    def get_customer(self, name):
        for c in self.customers:
            if c.name.lower() == name.lower():
                return c
        return None

    def add_customer_interaction(self, name, interaction):
        customer = self.get_customer(name)
        if customer is None:
            raise KeyError(f"Customer named {name} is not registered.")

        customer.add_interaction(interaction)
        return customer

    def get_interaction_list(self, name):
        customer = self.get_customer(name)
        if customer is None:
            raise KeyError(f"Customer named {name} is not registered.")

        return customer.interactions

    def get_customer_list(self):
        return self.customers


if __name__ == "__main__":
    system = CustomerDataSystem("CRM Demo")

    print("Creating customers...")
    customer_a = system.add_customer("Customer A", "customer.a@example.com", "0700000001")
    customer_b = system.add_customer("Customer B", "customer.b@example.com", "0700000002")
    customer_c = system.add_customer("Customer C", "customer.c@example.com", "0700000003")
    print(f"Customer added: {customer_a.name}")
    print(f"Customer added: {customer_b.name}")
    print(f"Customer added: {customer_c.name}")

    print("Updating contact details...")
    updated_customer = system.update_customer_contact("Customer A", phone="0700000099")
    print(f"Phone number updated for {updated_customer.name}: {updated_customer.phone}")

    print("Adding interactions...")
    system.add_customer_interaction("Customer A", "Initial contact – phone call")
    system.add_customer_interaction("Customer A", "Follow-up – email")
    system.add_customer_interaction("Customer B", "Support question – chat")
    print("Interactions added.")

    print("Showing interactions...")
    interactions = system.get_interaction_list("Customer A")
    if not interactions:
        print("Customer A has no registered interactions.")
    else:
        print("List of interactions for Customer A:")
        for i, interaction in enumerate(interactions, 1):
            print(f"{i}. {interaction}")

    customer_a_record = system.get_customer("Customer A")
    days = customer_a_record.days_since_last_interaction()

    if days is None:
        print("Days since last interaction (Customer A): No interactions")
    else:
        print(f"Days since last interaction (Customer A): {days}")

    print("Customer overview:")
    customers = system.get_customer_list()
    if not customers:
        print("There are no customers registered in the system.")
    else:
        for customer in customers:
            print(customer)

    print("Testing error handling...")

    try:
        system.add_customer("Customer X", "customer.a@example.com", "0700000098")
    except ValueError as e:
        print("Error:", e)

    try:
        system.remove_customer("Unknown Customer")
    except KeyError as e:
        print("Error:", e)

    try:
        system.add_customer_interaction("Unknown Customer", "Testing error")
    except KeyError as e:
        print("Error:", e)

    try:
        system.update_customer_contact("Unknown Customer", email="unknown@example.com", phone="0700000000")
    except KeyError as e:
        print("Error:", e)

    try:
        system.get_interaction_list("Unknown Customer")
    except KeyError as e:
        print("Error:", e)