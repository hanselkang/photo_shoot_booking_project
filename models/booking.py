class Booking:
    def __init__(self, name, address, num_of_group,  photoshoot_start_time,  photoshoot_end_time, client_id, service_id, photographer_id, id=None):
        self.name = name
        self.address = address
        self.num_of_group = num_of_group
        self.photoshoot_start_time = photoshoot_start_time
        self.photoshoot_end_time = photoshoot_end_time
        self.client_id = client_id
        self.service_id = service_id
        self.photographer_id = photographer_id
        self.id = id
