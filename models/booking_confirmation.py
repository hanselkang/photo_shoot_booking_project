class BookingConfirmation:
    def __init__(self, name, address, num_of_group,  photoshoot_start_time,  photoshoot_end_time, client, service, photographer, id=None):
        self.name = name
        self.address = address
        self.num_of_group = num_of_group
        self.photoshoot_start_time = photoshoot_start_time
        self.photoshoot_end_time = photoshoot_end_time
        self.client = client
        self.service = service
        self.photographer = photographer
        self.id = id
