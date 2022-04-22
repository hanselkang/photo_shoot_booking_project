class Booking:
    def __init__(self, name, num_of_group, address, client_id, service_id, photographer_id, id=None):
        self.name = name
        self.address = address
        self.num_of_group = num_of_group
        self.client_id = client_id
        self.service_id = service_id
        self.photographer_id = photographer_id
        self.id = id
