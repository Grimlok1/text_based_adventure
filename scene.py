class Scene:
    def __init__(self, text, options=None, reward=None):
        self.text = text
        self.options = options or {}
        self.reward = reward or []
        
def S(text, options=None, reward=None):
    return Scene(text, options, reward)