
import pickle

class Person:
    """
    Represents a person with basic attributes like ID, name, and contact information.
    """

    def __init__(self, ID, name, contact_info):
        """
        Initialize a Person object with ID, name, and contact information.
        """
        self.ID = ID
        self.name = name
        self.contact_info = contact_info

    def display_details(self):
        """
        Display details of the person.
        """
        print(f"ID: {self.ID}, Name: {self.name}, Contact Info: {self.contact_info}")


class Client(Person):
    """
    Represents a client who wants an event to be organized.
    """

    clients = []

    def __init__(self, ID, name, contact_info, budget):
        """
        Initialize a Client object with ID, name, contact information, and budget.
        """
        super().__init__(ID, name, contact_info)
        self.budget = budget
        self.events = []

    @classmethod
    def create_client(cls, ID, name, contact_info, budget):
        """
        Create a new client and add it to the list of clients.
        """
        client = cls(ID, name, contact_info, budget)
        cls.clients.append(client)
        return client

    @classmethod
    def update_client(cls, ID, name=None, contact_info=None, budget=None):
        """
        Update details of an existing client.
        """
        client = cls.find_client_by_id(ID)
        if client:
            if name:
                client.name = name
            if contact_info:
                client.contact_info = contact_info
            if budget:
                client.budget = budget
            print("Client updated successfully!")
        else:
            print("Client not found!")

    @classmethod
    def delete_client(cls, ID):
        """
        Delete a client from the list of clients.
        """
        client = cls.find_client_by_id(ID)
        if client:
            cls.clients.remove(client)
            print("Client deleted successfully!")
        else:
            print("Client not found!")

    @classmethod
    def find_client_by_id(cls, ID):
        """
        Find a client by ID.
        """
        for client in cls.clients:
            if client.ID == ID:
                return client
        return None

    def display_details_by_id(self, ID):
        """
        Display details of a client by ID.
        """
        client = self.find_client_by_id(ID)
        if client:
            client.display_details()
        else:
            print("Client not found!")


class Staff(Person):
    """
    Represents a staff member who organizes events.
    """

    staffs = []

    def __init__(self, ID, name, contact_info, role):
        """
        Initialize a Staff object with ID, name, contact information, and role.
        """
        super().__init__(ID, name, contact_info)
        self.role = role
        self.event_assigned = None

    @classmethod
    def create_staff(cls, ID, name, contact_info, role):
        """
        Create a new staff member and add it to the list of staffs.
        """
        staff = cls(ID, name, contact_info, role)
        cls.staffs.append(staff)
        return staff

    @classmethod
    def update_staff(cls, ID, name=None, contact_info=None, role=None):
        """
        Update details of an existing staff member.
        """
        staff = cls.find_staff_by_id(ID)
        if staff:
            if name:
                staff.name = name
            if contact_info:
                staff.contact_info = contact_info
            if role:
                staff.role = role
            print("Staff updated successfully!")
        else:
            print("Staff not found!")

    @classmethod
    def delete_staff(cls, ID):
        """
        Delete a staff member from the list of staffs.
        """
        staff = cls.find_staff_by_id(ID)
        if staff:
            cls.staffs.remove(staff)
            print("Staff deleted successfully!")
        else:
            print("Staff not found!")

    @classmethod
    def find_staff_by_id(cls, ID):
        """
        Find a staff member by ID.
        """
        for staff in cls.staffs:
            if staff.ID == ID:
                return staff
        return None

    def display_details_by_id(self, ID):
        """
        Display details of a staff member by ID.
        """
        staff = self.find_staff_by_id(ID)
        if staff:
            staff.display_details()
        else:
            print("Staff not found!")


class Guest(Person):
    """
    Represents a guest attending an event.
    """

    guests = []

    def __init__(self, ID, name, contact_info):
        """
        Initialize a Guest object with ID, name, and contact information.
        """
        super().__init__(ID, name, contact_info)
        self.events_attending = []

    @classmethod
    def create_guest(cls, ID, name, contact_info):
        """
        Create a new guest and add it to the list of guests.
        """
        guest = cls(ID, name, contact_info)
        cls.guests.append(guest)
        return guest

    @classmethod
    def update_guest(cls, ID, name=None, contact_info=None):
        """
        Update details of an existing guest.
        """
        guest = cls.find_guest_by_id(ID)
        if guest:
            if name:
                guest.name = name
            if contact_info:
                guest.contact_info = contact_info
            print("Guest updated successfully!")
        else:
            print("Guest not found!")

    @classmethod
    def delete_guest(cls, ID):
        """
        Delete a guest from the list of guests.
        """
        guest = cls.find_guest_by_id(ID)
        if guest:
            cls.guests.remove(guest)
            print("Guest deleted successfully!")
        else:
            print("Guest not found!")

    @classmethod
    def find_guest_by_id(cls, ID):
        """
        Find a guest by ID.
        """
        for guest in cls.guests:
            if guest.ID == ID:
                return guest
        return None

    def display_details_by_id(self, ID):
        """
        Display details of a guest by ID.
        """
        guest = self.find_guest_by_id(ID)
        if guest:
            guest.display_details()
        else:
            print("Guest not found!")


class Event:
    """
    Represents an event to be organized.
    """

    events = []

    def __init__(self, ID, event_name, event_date, client, venue):
        """
        Initialize an Event object with ID, event name, event date, client, and venue.
        """
        self.ID = ID
        self.event_name = event_name
        self.event_date = event_date
        self.client = client
        self.venue = venue
        self.guests = []
        self.staff = []
        self.suppliers = []

    @classmethod
    def create_event(cls, ID, event_name, event_date, client, venue):
        """
        Create a new event and add it to the list of events.
        """
        event = cls(ID, event_name, event_date, client, venue)
        cls.events.append(event)
        return event

    @classmethod
    def update_event(cls, ID, event_name=None, event_date=None, client=None, venue=None):
        """
        Update details of an existing event.
        """
        event = cls.find_event_by_id(ID)
        if event:
            if event_name:
                event.event_name = event_name
            if event_date:
                event.event_date = event_date
            if client:
                event.client = client
            if venue:
                event.venue = venue
            print("Event updated successfully!")
        else:
            print("Event not found!")

    @classmethod
    def delete_event(cls, ID):
        """
        Delete an event from the list of events.
        """
        event = cls.find_event_by_id(ID)
        if event:
            cls.events.remove(event)
            print("Event deleted successfully!")
        else:
            print("Event not found!")

    @classmethod
    def find_event_by_id(cls, ID):
        """
        Find an event by ID.
        """
        for event in cls.events:
            if event.ID == ID:
                return event
        return None

    def display_details_by_id(self, ID):
        """
        Display details of an event by ID.
        """
        event = self.find_event_by_id(ID)
        if event:
            event.display_details()
        else:
            print("Event not found!")

    def display_details(self):
        """
        Display details of the event.
        """
        print(f"Event ID: {self.ID}, Name: {self.event_name}, Date: {self.event_date}")
        self.client.display_details()
        self.venue.display_details()

    def add_guest(self, guest):
        """
        Add a guest to the list of guests attending the event.
        """
        self.guests.append(guest)

    def add_staff(self, staff):
        """
        Add a staff member to the list of staff assigned to the event.
        """
        self.staff.append(staff)

    def add_supplier(self, supplier):
        """
        Add a supplier to the list of suppliers for the event.
        """
        self.suppliers.append(supplier)


class Venue:
    """
    Represents a venue where an event can take place.
    """

    venues = []

    def __init__(self, ID, venue_name, capacity, location):
        """
        Initialize a Venue object with ID, venue name, capacity, and location.
        """
        self.ID = ID
        self.venue_name = venue_name
        self.capacity = capacity
        self.location = location

    @classmethod
    def create_venue(cls, ID, venue_name, capacity, location):
        """
        Create a new venue and add it to the list of venues.
        """
        venue = cls(ID, venue_name, capacity, location)
        cls.venues.append(venue)
        return venue

    @classmethod
    def update_venue(cls, ID, venue_name=None, capacity=None, location=None):
        """
        Update details of an existing venue.
        """
        venue = cls.find_venue_by_id(ID)
        if venue:
            if venue_name:
                venue.venue_name = venue_name
            if capacity:
                venue.capacity = capacity
            if location:
                venue.location = location
            print("Venue updated successfully!")
        else:
            print("Venue not found!")

    @classmethod
    def delete_venue(cls, ID):
        """
        Delete a venue from the list of venues.
        """
        venue = cls.find_venue_by_id(ID)
        if venue:
            cls.venues.remove(venue)
            print("Venue deleted successfully!")
        else:
            print("Venue not found!")

    @classmethod
    def find_venue_by_id(cls, ID):
        """
        Find a venue by ID.
        """
        for venue in cls.venues:
            if venue.ID == ID:
                return venue
        return None

    def display_details(self):
        """
        Display details of the venue.
        """
        print(f"Venue ID: {self.ID}, Name: {self.venue_name}, Capacity: {self.capacity}, Location: {self.location}")

    def display_details_by_id(cls, ID):
        """
        Display details of a venue by ID.
        """
        venue = cls.find_venue_by_id(ID)
        if venue:
            venue.display_details()
        else:
            print("Venue not found!")


class Supplier:
    """
    Represents a supplier providing services for an event.
    """

    suppliers = []

    def __init__(self, ID, name, service_type, contact_info):
        """
        Initialize a Supplier object with ID, name, service type, and contact information.
        """
        self.ID = ID
        self.name = name
        self.service_type = service_type
        self.contact_info = contact_info

    @classmethod
    def create_supplier(cls, ID, name, service_type, contact_info):
        """
        Create a new supplier and add it to the list of suppliers.
        """
        supplier = cls(ID, name, service_type, contact_info)
        cls.suppliers.append(supplier)
        return supplier

    @classmethod
    def update_supplier(cls, ID, name=None, service_type=None, contact_info=None):
        """
        Update details of an existing supplier.
        """
        supplier = cls.find_supplier_by_id(ID)
        if supplier:
            if name:
                supplier.name = name
            if service_type:
                supplier.service_type = service_type
            if contact_info:
                supplier.contact_info = contact_info
            print("Supplier updated successfully!")
        else:
            print("Supplier not found!")

    @classmethod
    def delete_supplier(cls, ID):
        """
        Delete a supplier from the list of suppliers.
        """
        supplier = cls.find_supplier_by_id(ID)
        if supplier:
            cls.suppliers.remove(supplier)
            print("Supplier deleted successfully!")
        else:
            print("Supplier not found!")

    @classmethod
    def find_supplier_by_id(cls, ID):
        """
        Find a supplier by ID.
        """
        for supplier in cls.suppliers:
            if supplier.ID == ID:
                return supplier
        return None

    def display_details(self):
        """
        Display details of the supplier.
        """
        print \
            (f"Supplier ID: {self.ID}, Name: {self.name}, Service Type: {self.service_type}, Contact Info: {self.contact_info}")

    @classmethod
    def display_details_by_id(cls, ID):
        """
        Display details of a supplier by ID.
        """
        supplier = cls.find_supplier_by_id(ID)
        if supplier:
            supplier.display_details()
        else:
            print("Supplier not found!")

def save_data(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_data(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data

# Example Usage:
if __name__ == "__main__":
    # Create instances using create methods
    client1 = Client.create_client(1, "Client 1", "client1@example.com", 10000)
    staff1 = Staff.create_staff(1, "Staff 1", "staff1@example.com", "Event Coordinator")
    guest1 = Guest.create_guest(1, "Guest 1", "guest1@example.com")
    venue1 = Venue.create_venue(1, "Venue 1", 200, "Location 1")
    supplier1 = Supplier.create_supplier(1, "Supplier 1", "Catering", "supplier1@example.com")
    event1 = Event.create_event(1, "Event 1", "2024-05-03", client1, venue1)

    # Add associations
    # client1.create_event(event1)
    event1.add_staff(staff1)
    event1.add_guest(guest1)
    event1.add_supplier(supplier1)

    # Display details
    print("Client Details:")
    client1.display_details()
    print("\nEvent Details:")
    event1.display_details()
    print("\nStaff Details:")
    staff1.display_details()
    print("\nGuest Details:")
    guest1.display_details()
    print("\nVenue Details:")
    venue1.display_details()
    print("\nSupplier Details:")
    supplier1.display_details()

    # Save data to a binary file
    save_data((Client.clients, Staff.staffs, Guest.guests, Event.events, Venue.venues, Supplier.suppliers), 'data.pkl')



    # Update and delete examples
    print("\nUpdate and Delete Examples:")
    Client.update_client(1, name="Updated Client")
    client1.display_details()
    Staff.delete_staff(1)
    Staff.delete_staff(2)  # Testing non-existent staff deletion

    # Display details by ID examples
    print("\nDisplay Details by ID Examples:")
    client1.display_details_by_id(1)
    staff1.display_details_by_id(1)
    guest1.display_details_by_id(1)
    venue1.display_details_by_id(1)
    supplier1.display_details_by_id(1)
    print("\n")
    event1.display_details_by_id(1)

