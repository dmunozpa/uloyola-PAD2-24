class Terminal:
    def __init__(self, phone_number:str):

        if not self.validate_phone_number(phone_number):
            raise ValueError("Invalid phone number. Please enter a valid 9-digit number starting with 9, 6, or 7.")
        
        self.phone_number = phone_number
        self.conversation_time = 0

    # Method validate PhoneNumber
    def validate_phone_number(self, phone_number:str)->bool:
        result = False
        # Review the conditions - (only digits, starting with 9, 6, or 7, and their lengthis nine digit
        if(phone_number.isdigit() and phone_number[0] in ('9', '6', '7') and len(phone_number) == 9):
            result = True
        return result

    # Method Call with other_terminal
    def call(self, other_terminal, duration:int):
        self.conversation_time += duration
        other_terminal.conversation_time += duration

    # Method String
    def __str__(self):
        return f"{self.phone_number} - Conversation time: {self.conversation_time}s"

    # Method String
    def __repr__(self):
        return f"{self.phone_number} - Conversation time: {self.conversation_time}s"



# Test program
if __name__ == "__main__":
    t1 = Terminal("666112233")
    t2 = Terminal("666744459")
    t3 = Terminal("632128919")
    t4 = Terminal("664135818")

    print(t1)
    print(t2)

    t1.call(t2, 420)
    t1.call(t3, 210)

    print(t1)
    print(t2)
    print(t3)
    print(t4)
