class Event:
    #lisää myöhemmin mahdollisuus lisätä monta kuvausta... ehkä
    def __init__(self, description, required_flags=None, flag=None):
        self.description = description
        self.options = []
        self.treasure = []
        self.flag = flag
        self.required_flags = set(required_flags or [])
        self.visited = False

    def resolve(self, game):
        if self.flag:
            game.flags.add(self.flag)

        if not self.visited:
            for treasure in self.treasure:
                game.inventory.update({str(len(game.inventory) + 1) : treasure})
            self.visited = True

    def add_next_event(self, next_event):
        self.options.append(self.Option("Continue", next_event))
        
    def add_option(self, description, next_event, required_flags=[]):
        self.options.append(self.Option(description, next_event, required_flags))
        
    def add_treasure(self, name, description):
        self.treasure.append(self.Treasure(name, description))

    def get_treasure(self):
        if not self.visited:
            self.visited = True
            return self.treasure

    def get_options(self, flags):
        available_options = {}
        i = 1
        for option in self.options:
            if option.required_flags.issubset(flags):
                available_options[str(i)] = option
                i = i + 1
        return available_options

    class Option:
        def __init__(self, description, def_event, alt_events=None, required_flags=None):
            self.description = description
            self.def_event = def_event
            self.alt_events = alt_events or []

            self.required_flags = set(required_flags or [])

        def get_next_event(self, flags):
            next_event = self.def_event
            for event in self.alt_events:
                if event.required_flags.issubset(flags):
                    next_event = event
                    break
            return next_event

    class Treasure:
        def __init__(self, name, description):
            self.name = name
            self.description = description
            
class Game:
    def __init__(self):
        self.flags = set()
        self.inventory = {}
        self.events = {}
        self.current_event = None

    def create_event(self,name, description, required_flags=None, flag=None):
        event = Event(description, required_flags, flag)
        self.events[name] = event
        return event