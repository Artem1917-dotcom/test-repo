from Lesson3.Address import Address

class Mailing:
    def __init__(self, to_address: Address, from_address: Address, cost: float, track: str):
        if not isinstance(to_address, Address):
            raise TypeError("to_address должен быть типа Address")
        if not isinstance(from_address, Address):
            raise TypeError("from_address должен быть типа Address")
        if not isinstance(cost, (int, float)):
            raise TypeError("cost должен быть числом")
        if not isinstance(track, str):
            raise TypeError("track должен быть строкой")
            
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track