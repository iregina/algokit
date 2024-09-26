from algopy import ARC4Contract, String, UInt64, Box, arc4
from algopy.arc4 import abimethod


class HelloWorld(ARC4Contract):

    def __init__(self) -> None:
        # Pseucode: Instantiate a Box to store an array of 32-bit unsigned integers
         self.cool_box = Box(arc4.String, key="key")

    @abimethod()
    def hello(self, name: String) -> String:
        greeting = "Hello, " + name
        #Pseudocode: store value in Box
        # self.cool_box.value = arc4.String(greeting)
        return greeting
