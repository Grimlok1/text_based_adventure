import text
from scene import S

story = {
	"footsteps": S(text.FOOTSTEPS, {"hide" : "hide", "wait" : "wait"}),											
	"hide": S(text.HIDE, {"follow": "follow_dict"}),
	"wait": S(text.WAIT, {"tell him the truth" : "truth", "lie" : "lie"}),
    "truth": S(text.TRUTH, reward=["golden token"]),
    "lie": S(text.LIE, {"tell him the truth" : "truth", "lie again" : "lie_again"}), 
    "lie_again": S(text.LIE2),
}