"""
CIS 3400 - Advanced Programming
Object-Oriented Programming Pair Assignment

Phone Repair Shop

Name:
"""


# ==========================================================
# CUSTOMER CLASS
# ==========================================================

class Customer:
    """Represents a customer of the phone repair shop."""

    def __init__(self, customer_id, name, phone, email):

        # TODO:
        # Create instance attributes for:
        # customer_id
        # name
        # phone
        # email

        pass


    def __str__(self):

        # TODO:
        # Return a readable description of the customer.

        pass



# ==========================================================
# REPAIR ORDER CLASS
# ==========================================================

class RepairOrder:
    """Represents one phone repair order."""

    # Class attributes shared by all RepairOrder objects.

    SERVICE_PRICES = {
        "screen replacement": 129.00,
        "battery replacement": 79.00,
        "os update": 49.00,
        "data transfer": 59.00
    }

    RUSH_FEE = 30.00


    def __init__(
        self,
        repair_id,
        customer,
        device,
        date_in,
        service,
        rush_service=False,
        extra_charge=0.00
    ):

        # TODO:
        # Create instance attributes for:
        #
        # repair_id
        # customer
        # device
        # date_in
        # date_out
        # service
        # rush_service
        # extra_charge
        #
        # Remember:
        # date_out should begin as None.
        #
        # Consider converting service to lowercase
        # so it matches the keys in SERVICE_PRICES.

        pass


    def calculate_charge(self):
        """
        Calculate and return the total repair charge.

        Total Charge =
        Base Service Price
        + Rush Fee, if requested
        + Extra Charge
        """

        # TODO:
        #
        # Step 1:
        # Find the base price using SERVICE_PRICES.
        #
        # Step 2:
        # If rush_service is True,
        # add the RUSH_FEE.
        #
        # Step 3:
        # Add the extra_charge.
        #
        # Step 4:
        # Return the total.

        pass


    def complete_repair(self, date_out):
        """Record the date the repair was completed."""

        # TODO:
        # Change the object's date_out attribute.

        pass


    def __str__(self):

        # TODO:
        #
        # Return readable information containing:
        #
        # Repair ID
        # Customer name
        # Device
        # Service
        # Date in
        # Date out
        # Rush Service: Yes or No
        # Extra Charge
        # Total Charge

        pass



# ==========================================================
# MAIN PROGRAM
# ==========================================================


# ----------------------------------------------------------
# STEP 1: Create at least THREE Customer objects.
# ----------------------------------------------------------

# TODO



# ----------------------------------------------------------
# STEP 2: Display your Customer objects.
# ----------------------------------------------------------

print("\nCUSTOMERS")
print("=" * 50)

# TODO



# ----------------------------------------------------------
# STEP 3: Create at least FIVE RepairOrder objects.
# ----------------------------------------------------------

# Requirements:
#
# - Use at least 3 customers.
# - One customer must have TWO repair orders.
# - At least one order must use rush service.
# - At least one order must have an extra charge.
# - Use at least three different services.

# TODO



# ----------------------------------------------------------
# STEP 4: Mark at least TWO repairs as completed.
# ----------------------------------------------------------

# Example:
#
# repair1.complete_repair("09/14/2026")

# TODO



# ----------------------------------------------------------
# STEP 5: Display all RepairOrder objects.
# ----------------------------------------------------------

print("\nREPAIR ORDERS")
print("=" * 50)

# TODO
