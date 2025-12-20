class Event:
    #lisää myöhemmin mahdollisuus lisätä monta kuvausta... ehkä
    def __init__(self, description, *flags):
        self.description = description
        self.options = []
        self.treasure = []
        self.flag = set(flags)
        self.next_event = None
        
        
    def add_next_event(self, next_event):
        self.next_event = next_event
        
    def add_option(self, description, next_event, required_flags=[]):
        self.options.append(self.Option(description, next_event, required_flags))
        
    def add_treasure(self, name, description):
        self.treasure.append(self.Treasure(name, description))
        
    def get_options(self, flags):
        return [
            option for option in self.options
            if option.required_flags.issubset(flags)
        ]
        
    class Option:
        def __init__(self, description, next_event, required_flags=None):
            self.description = description
            self.next_event = next_event
            self.required_flags = set(required_flags or [])
            
    class Treasure:
        def __init__(self, name, description):
            self.name = name
            self.description = description
            
class Game:
    def __init__(self, current_event):
        self.flags = set()
        self.inventory = []
        self.current_event = current_event