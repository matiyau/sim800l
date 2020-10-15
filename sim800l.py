#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 00:23:55 2020

@author: n7
"""

import serial

class SIM800L():
    """Class interface for SIM800L module

    """

    def __init__(self, port, baud):
        """Initializes the class instance

        Parameters:
            port (str): Serial port of the module.
            baud (int): Baud rate for communicating with the module.

        """
        serial.Serial.__init__(self)
        self.port = port
        self.baudrate = baud

    def send_sms(tel_num):
        """Sends text SMS to the given telephone number

        Parameters:
            tel_num (str): Telephone number to which the SMS is to be sent
                           (with country code).

        """
        self.open()
            
        self.close()

    def add_lock(new_pin, old_pin=None)
        """Adds a PIN lock to the SIM Card

        Parameters:
            new_pin (str): Numeric PIN for locking the SIM card.
                           [PIN should be passed as a string].
            old_pin (str, optional): Old PIN if the SIM Card already has a 
                                     a PIN lock on it. This parameter is not
                                     required if no existing lock is present
                                     on the SIM
                                     [PIN should be passed as a string].

        """
        self.open()
            
        self.close()

    def remove_lock(pin):
        """Remove a PIN lock from the SIM Card

        Parameters:
            pin (str): Existing PIN for the SIM card.
                       [PIN should be passed as a string].

        """
        self.open()
            
        self.close()

    def unlock(pin):
        """Unlock the SIM Card for usage.

        Parameters:
            pin (str): Numeric PIN for unlocking the SIM card.
                       [PIN should be passed as a string].

        """
        self.open()
            
        self.close()

