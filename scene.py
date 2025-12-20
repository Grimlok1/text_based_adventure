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
        
    def add_option(self, description, next_event, flags=[]):
        self.options.append(self.Option(description, next_event, flags))
        
    def add_treasure(self, name, description):
        self.treasure.append(self.Treasure(name, description))
        
    def get_options(self, flags):
        return [
            option for option in self.options
            if not option.flags or option.flags.issubset(flags)
        ]
    def event_description(self):
        print(self.description)
        self.game.add_flags(self.flag)
        for treasure in self.treasure:
            print(f"{treasure.name} added to the inventory")
            self.game.add_treasure(treasure )
               
    class Option:
        def __init__(self, description, next_event, flags):
            self.description = description
            self.next_event = next_event
            self.flags = flags
            
    class Treasure:
        def __init__(self, name, description):
            self.name = name
            self.description = description
            
class Game:
    def __init__(self):
        self.flags = set()
        self.inventory = []
        
    def add_flags(self, flags):
        self.flags.update(flags)
        
    def add_treasure(self, treasure):
        self.inventory.append(treasure)