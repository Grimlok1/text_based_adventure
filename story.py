import text
from scene import SCENE, Option, Target

story = dict([
	SCENE("footsteps", text.FOOTSTEPS,
        Option("hide", Target("hide")),
        Option("wait", Target("wait")),
        ),
       
    SCENE("hide", text.HIDE,
        Option("follow the man", Target("follow"))
        ),
        
	SCENE("wait", text.WAIT,
        Option("tell him the truth", Target("truth")),
        Option("lie", Target("lie"))
        ),
        
    SCENE("follow", text.FOLLOW,
        Option("carry on walking forward", Target("bear_attack", ["lied_to_man"]), Target("bear"), Target("bear_friendly", ["true"]))
        ),
    
    SCENE("bear", text.BEAR_NORMAL),
    
    SCENE("bear_attack", text.BEAR_ATTACK),
    
    SCENE("bear_friendly", text.BEAR_FRIENDLY),
    
    SCENE("truth", text.TRUTH,
        Option("carry on walking forward", Target("bear_attack", ["lied_to_man"]), Target("bear"), Target("bear_friendly", ["true"])),
        reward=["Golden token"],
        set_flags=["true"],
        ),
        
    SCENE("lie", text.LIE,
        Option("tell him the truth", Target("truth")),
        Option("lie again", Target("lie2")),
        ),
        
    SCENE("lie2", text.LIE2,
        Option("carry on walking forward", Target("bear_attack", ["lied_to_man"]), Target("bear_friendly", ["true"]), Target("bear")),
        set_flags=["lied_to_man"],
    ),
    
       
])