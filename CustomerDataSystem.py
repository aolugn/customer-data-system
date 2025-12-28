# Customer Data System – Educational assignment (demo data anonymized

from datetime import datetime


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

    def days_since_last_interaction(self):
        if self.last_interaction is None:
            return None
        else:
            return (datetime.now() - self.last_interaction).days


class CustomerDataSystem:
    def __init__(self, name: str):
        self.name = name
        self.customers = []

    def add_customer(self, name, email, phone):
        for e in self.customers:
            if e.email.lower() == email.lower():
                raise ValueError(f"A customer with email address {email} is already registered.")
        self.customers.append(Customer(name, email, phone))
        print(f"Customer added: {name}")

    def remove_customer(self, name):
        c = self.get_customer(name)
        if c is None:
            raise KeyError(f"Customer named {name} is not registered.")
        self.customers.remove(c)
        print(f"Customer removed: {name}")

    def update_customer_contact(self, name, email=None, phone=None):
        c = self.get_customer(name)
        if c is None:
            raise KeyError(f"Customer named {name} is not registered.")

        if email is not None:
            c.email = email
            print(f"Email updated for {name}: {email}")

        if phone is not None:
            c.phone = phone
            print(f"Phone number updated for {name}: {phone}")

    def get_customer(self, name):
        for c in self.customers:
            if c.name.lower() == name.lower():
                return c
        return None

    def add_customer_interaction(self, name, interaction):
        c = self.get_customer(name)
        if c is None:
            raise KeyError(f"Customer named {name} is not registered.")
        c.add_interaction(interaction)
        print(f"Interaction added for {name}.")

    def get_interaction_list(self, name):
        c = self.get_customer(name)
        if c is None:
            raise KeyError(f"Customer named {name} is not registered.")

        if len(c.interactions) == 0:
            print(f"{name} has no registered interactions.")
            return []

        print(f"List of interactions for {name}:")
        for i, interaction in enumerate(c.interactions, 1):
            print(f"{i}. {interaction}")

        return c.interactions

    def get_customer_list(self):
        if len(self.customers) == 0:
            print("There are no customers registered in the system.")
            return

        print("Customer list:")
        for c in self.customers:
            print(c)


if __name__ == "__main__":
    system = CustomerDataSystem("CRM Demo")

    print("Creating customers...")
    system.add_customer("Customer A", "customer.a@example.com", "0700000001")
    system.add_customer("Customer B", "customer.b@example.com", "0700000002")
    system.add_customer("Customer C", "customer.c@example.com", "0700000003")

    print("Updating contact details...")
    system.update_customer_contact("Customer A", phone="0700000099")

    print("Adding interactions...")
    system.add_customer_interaction("Customer A", "Initial contact – phone call")
    system.add_customer_interaction("Customer A", "Follow-up – email")
    system.add_customer_interaction("Customer B", "Support question – chat")

    print("Showing interactions...")
    system.get_interaction_list("Customer A")

    customer_a = system.get_customer("Customer A")
    days = customer_a.days_since_last_interaction()

    if days is None:
        print("Days since last interaction (Customer A): No interactions")
    else:
        print(f"Days since last interaction (Customer A): {days}")

    print("Customer overview:")
    system.get_customer_list()

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