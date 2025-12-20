from scene import Event
import text
#events

start = Event(text.START)
truth = Event(text.TRUTH)
tell_truth = Event(text.TELL_TRUTH)
tell_lie = Event(text.TELL_LIE)

start.add_next_event(truth)
start.add_treasure("flask", "Old iron flask")
start.add_treasure("iron amule", "Old, heavy, rugged amulet, shaped in the likeness of a sitting bear")
truth.add_option("lie to the man", tell_lie)
truth.add_option("Show him the amulet", tell_truth)
