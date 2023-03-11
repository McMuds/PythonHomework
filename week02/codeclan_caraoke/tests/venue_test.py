import unittest
from src.venue import Venue
from src.room import Room
from src.guest import Guest

class TestVenue(unittest.TestCase):
    
    def setUp(self):
        self.venue1 = Venue("Karaoke Karnage",100.0)
        self.room1 = Room(1,[],[])
        self.guest1 = Guest("Katie Perry", 50)

    def test_venue_has_name(self):
        self.assertEqual("Karaoke Karnage",self.venue1.name)

    def test_venue_has_money(self):
        self.assertEqual(100.0,self.venue1.till)

    def test_venue_has_rooms(self):
        self.venue1.add_room(self.room1)
        self.assertEqual(1,len(self.venue1.rooms))

    def test_can_add_money_to_till(self):
        self.venue1.add_money_to_till(10)
        self.assertEqual(110,self.venue1.till)
