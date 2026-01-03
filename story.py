from scene import Event, Game
import text

game = Game() #Game object

#Events
start = game.create_event("start", text.START)
hunter = game.create_event("hunter", text.HUNTER)
show_amulet = game.create_event("show_amulet", text.SHOW_AMULET)
ask_again = game.create_event("ask_again", text.ASK_AGAIN)
keep_amulet = game.create_event("Keep_amulet", text.KEEP_AMULET)
show_amulet_2 = game.create_event("show_amulet_2", text.SHOW_AMULET_2)
invite = game.create_event("invite", text.INVITE)
tale = game.create_event("tale", text.TALE)


#add options and items to the events
start.add_next_event(hunter)
start.add_treasure("flask", "Old iron flask")
start.add_treasure("iron amulet", "Old, heavy, rugged amulet, shaped in the likeness of a sitting bear")

hunter.add_option("Lie about the amulet", ask_again)
hunter.add_option("Show him the amulet", show_amulet)

show_amulet.add_next_event(invite)

ask_again.add_option("Lie again", keep_amulet)
ask_again.add_option("Show him the amulet", show_amulet_2)

keep_amulet.add_next_event(invite)
show_amulet_2.add_next_event(invite)

invite.add_next_event(tale)
