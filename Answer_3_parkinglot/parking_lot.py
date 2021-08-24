from slot import Slot
from car import Car


class Parking(object):
    """
    Parking class which has details about parking slots
    as well as operation performed on parking are present here
    """

    def __init__(self):
        self.slots = {}

    def _is_parking_lot_created(self):
        if len(self.slots) == 0:
            print("Parking Lot not created")
            return False
        return True

    def create_parking_lot(self, no_of_slots):
        """This method will create parking lot if not present already with given
        number of slots.
        Input: no_of_slots - Integer Type
        """
        no_of_slots = int(no_of_slots)

        if len(self.slots) > 0:
            print("Parking Lot already created")
            return

        if no_of_slots <= 0:
            print("Number of slots provided is incorrect.")
            return

        if no_of_slots > 0:
            for slot_no in range(1, no_of_slots + 1):
                new_slot = Slot(slot_no=slot_no, available=True)
                self.slots[slot_no] = new_slot
            print(f"Created a parking lot with {no_of_slots} slots")

    def get_nearest_available_slot(self):
        """Method to find nearest available slot in parking
        """
        available_slots = filter(lambda x: x.available, self.slots.values())
        if not available_slots:
            return None
        nearest_slot = sorted(available_slots, key=lambda x: x.slot_no)[0]
        return nearest_slot

    def park(self, registration_no, colour):
        """Method to park a coming car in nearest available parking
        slot. If not present it will throw message.
        Input: reg_no - String Type
               colour - String Type
        """

        if not self._is_parking_lot_created():
            return

        available_slot = self.get_nearest_available_slot()
        if available_slot:
            # create car object and save in the available slot
            available_slot.car = Car(registration_no, colour)
            available_slot.available = False
            print(f"Allocated slot number: {available_slot.slot_no}")
        else:
            print("Sorry, parking lot is full.")

    def leave(self, slot_no):
        """Method to empty a parking slot while car is leaving.
        Input: slot_no - Integer Type
        """
        slot_no = int(slot_no)
        if not self._is_parking_lot_created():
            return

        if slot_no not in self.slots:
            print("Sorry, slot number does not exist in parking lot.")
            return

        slot = self.slots[slot_no]
        if not slot.available and slot.car:
            slot.car = None
            slot.available = True
            print(f"Slot number is free {slot_no}")
        else:
            print(f"No car is present at slot number {slot_no}")

    def status(self):
        """Method to show current status of parking
        """
        if not self._is_parking_lot_created():
            return

        print("Slot No\tRegistration No\tColour")
        for slot in self.slots.values():
            if not slot.available and slot.car:
                print(f"{slot.slot_no} \t {slot.car.registration_no} \t {slot.car.colour}")

    def registration_numbers_for_cars_with_colour(self, colour):
        """Method to find registration numbers of car with given colour in
        parking
        Input: colour - String Type
        """

        if not self._is_parking_lot_created():
            return

        registration_nos = []
        for slot in self.slots.values():
            if not slot.available and slot.car and \
                    slot.car.colour == colour:
                registration_nos.append(slot.car.registration_no)

        if len(registration_nos) > 0:
            print(' '.join(registration_nos))
        else:
            print("Not found")

    def slot_numbers_for_cars_with_colour(self, colour):
        """Method to find slot numbers for cars with given colour in
        parking.
        Input: colour - String Type
        """

        if not self._is_parking_lot_created():
            return

        slot_nos = []
        for slot in self.slots.values():
            if not slot.available and slot.car and \
                    slot.car.colour == colour:
                slot_nos.append(slot.slot_no)

        if len(slot_nos) > 0:
            print(' '.join(slot_nos))
        else:
            print("Not found")

    def slot_number_for_registration_number(self, registration_no):
        """Method to find slot numbers in parking with given registration
        number.
        Input: reg_no - String Type
        """

        if not self._is_parking_lot_created():
            return

        slot_no = ''
        for slot in self.slots.values():
            if not slot.available and slot.car and \
                    slot.car.registration_no == registration_no:
                slot_no = slot.slot_no
                break

        if slot_no:
            print(slot_no)
        else:
            print("Not found")
