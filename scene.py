class Scene:
    def __init__(self, text, options=None, reward=None, set_flags=None):
        self.text = text
        self.options = options or {}
        self.reward = reward or []
        self.set_flags = set_flags or []
        
class Option:
    def __init__(self, label, *targets, conditions=None):
        self.label = label
        self.targets = list(targets)
        self.conditions = conditions or []
        
class Target:
    def __init__(self, scene, conditions=None):
        self.scene = scene
        self.conditions = conditions or []
        
def SCENE(name, text, *options, reward=None, targets=None, set_flags=None):
    return (name, Scene(text, list(options), reward, set_flags))