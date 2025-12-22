from scene import Event, Game
import text
#events

start = Event(text.START)
hunter = Event(text.HUNTER)
tell_truth = Event(text.TELL_TRUTH)
tell_lie = Event(text.TELL_LIE)

#game object
game = Game(start)

#add next event add continue default option too
start.add_next_event(hunter)
start.add_treasure("flask", "Old iron flask")
start.add_treasure("iron amule", "Old, heavy, rugged amulet, shaped in the likeness of a sitting bear")
hunter.add_option("lie to the man", tell_lie)
hunter.add_option("Show him the amulet", tell_truth)
