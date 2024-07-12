'''
To attract tourists, a casino in Las Vegas proposes an all-you-can-eat
buffet where guests only pay what they want to pay.

Given what each guest is ready to pay, you have to compute the restaurant's
gains for the day:

* At the beginning of the day the restaurant is empty.
* A guest arrives, finds a seat, eats, pays and then leaves.
* There are only nb_seats seats available. Guests can only eat and pay when
  they can be seated.
    * A guest which enters the restaurant and cannot find a seat waits in line
      until a seat is made available or until he/she gets bored and leaves.
    * A guest may come several times during the day, in that case, he/she will
      pay at most once.

Implement the function compute_day_gains which returns the gains for the day:

    * The array paying_guests gives what guests are ready to pay
      (for example if paying_guests[5] value is 25, it means that guest with
      id 5 is ready to pay $25 for the buffet.
    * The array guest_movements gives in order the arrivals and departures of
      guests. The first time you see an id, it indicates an arrival.
    * The second time you see the same id, it indicates a departure. An arrival
      is always followed later in the day by a departure.
'''


def compute_day_gains(nb_seats, paying_guests, guest_movements):
    """Calculate the day's earnings.

    Args:
        nb_seats (int): The number of seats in the restaurant
        paying_guests (list[int]): The amount a guest will be willing to pay
        guest_movements (list[int]): The order of arrivals and departures by
                                     guest

    Returns:
        total (int): The earnings for the day
    """

    # Tracks the guests as they enter and exit the restaurant
    guest_tracker = {}
    # Tracks the number of seats in use at the restaurant
    seats_in_use = 0
    # Stores and returns the total daily earnings
    total = 0

    # Iterate through the list of guest movements
    for guest in guest_movements:
        # Confirm that there's an available seat
        if seats_in_use < nb_seats:
            if guest in guest_tracker:
                # Existing customer!
                # Add 1 to the guest_tracker dict
                guest_tracker[guest] += 1

                # Check to see if the guest is leaving or entering
                # If mod 2 = 0, that means the guest has entered and exited
                # If mod 2 = 1, the means the guest has just entered the
                # restaurant
                if guest_tracker[guest] % 2 == 0:
                    # Free up a seat
                    seats_in_use -= 1
                else:
                    # Allocate a seat
                    seats_in_use += 1
            else:
                # New customer!
                # Add an entry to the guest_tracker
                # Allocate a seat for the guest
                guest_tracker[guest] = 1
                seats_in_use += 1

    # Iterate through the guest_tracker dict by item as a tuple.
    # The 1st tuple item is the guest ID from guest_movements
    # The 2nd tuple item is the number of visits
    for guest in guest_tracker.items():
        # Confirm that the guest has entered and exited
        # the restaurant at least once.
        if guest[1] > 1:
            # Add the amount the guest paid to the total, derived
            # from the guest's payment amount in the paying_guests list
            try:
                total += paying_guests[guest[0]]
            except IndexError:
                print(f'Missing payment information for guest {guest[0]}')
                continue

    return total


def main():
    """Main function.
    """
    nb_seats = 100
    paying_guests = [25, 10, 5, 30, 15]
    guest_movements = [4, 4, 3, 2, 3, 0, 0, 2, 4, 4, 3, 7, 7, 3]

    result = compute_day_gains(nb_seats, paying_guests, guest_movements)

    print(f'Total Earnings: ${result}')


if __name__ == "__main__":
    main()
