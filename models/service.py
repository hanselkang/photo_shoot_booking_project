class Service:
    def __init__(self, photo_type, hours, place, price, photographer_id, id=None):
        self.photo_type = photo_type
        self.place = place
        self.hours = hours
        self.price = price
        self.photographer_id = photographer_id
        self.id = id
