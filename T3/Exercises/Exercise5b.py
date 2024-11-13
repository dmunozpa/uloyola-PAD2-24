class Terminal:
    def __init__(self, phone_number:str):

        if not self._validatephone_number(phone_number):
            raise ValueError("Invalid phone number. Please enter a valid 9-digit number starting with 9, 6, or 7.")
        
        self.phone_number = phone_number
        self.conversation_time = 0

    # Method validate PhoneNumber
    def _validatephone_number(self, phone_number:str)->bool:
        result = False
        # Review the conditions - (only digits, starting with 9, 6, or 7, and their lengthis nine digit
        if(phone_number.isdigit() and phone_number[0] in ('9', '6', '7') and len(phone_number) == 9):
            result = True
        return result

    # Method Call with other_terminal
    def call(self, other_terminal, duration:int):

        self.conversation_time += duration
        other_terminal._conversation_time += duration

    # Method String
    def __str__(self):
        return f"{self.phone_number} - Conversation time: {self.conversation_time}s"


'''' Resolution for the Second Step'''

class Mobile(Terminal):

    # The cost per minute is 5, 15, and 30 cents,
 
    #Constructor
    def __init__(self, phone_number:Terminal, rate:str):
        super().__init__(phone_number)
        self.tariff_rates = {"rat": 0.05, "monkey": 0.15, "elephant": 0.30}
        self.rate = rate
        self.cost = 0

    #Call Metohd for Mobile phones
    def call(self, other_terminal:Terminal, duration:float):

        # Verify if the input is a Terminal
        if not isinstance(other_terminal, Mobile):
            raise ValueError("Invalid argument. Please provide a valid Mobile object.")
        
        # Get the Tafif crom tariff_rates
        cost_per_minute = self.tariff_rates[self.rate]

        cost_call = (duration / 60) * cost_per_minute
        self.conversation_time += duration
        other_terminal.conversation_time += duration

        self.cost = self.cost + cost_call

    # Change Rate Metof
    def changerate(self, newrate:str):
        if newrate not in self.tariff_rates:
            raise ValueError("Invalid rate. Please choose 'rat', 'monkey', or 'elephant'.")
        
        self.rate = newrate

    # Redefition of String, adding the charged cost with 2 digits
    def __str__(self):
        return f"{super().__str__()} - charged {self.cost:.2f}€"

    def __repr__(self):
        return f"{super().__str__()} - charged {self.cost:.2f}€"

# Test program
if __name__ == "__main__":

    m1 = Mobile("666112233", "rat")
    m2 = Mobile("666744459", "monkey")
    m3 = Mobile("632128919", "elephant")
    print(m1)
    print(m2)
    m1.call(m2, 210)
    m1.call(m3, 320)
    m2.call(m3, 450)
    print(m1)
    print(m2)
    print(m3)
