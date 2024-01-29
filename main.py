import pandas as pd

df = pd.read_csv("hotels.csv", dtype={'id': str})


class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id']==self.hotel_id, 'name'].squeeze()

    def book(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv("hotels.csv", index=False)

    def available(self):
        avail = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if avail in 'yes':
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, name_customer, hotel_object):
        self.name_customer = name_customer
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for reservation
        your booking credential are
        Name : {self.name_customer}
        Hotel Name : {self.hotel.name}
"""
        return content


print(df)
hotel_iD = input("enter the hotel id : ")
hotel = Hotel(hotel_iD)

if hotel.available():
    hotel.book()
    name = input("enter the name ")
    reserve = ReservationTicket(name, hotel)
    print(reserve.generate())

else:
    print("not available: ")
