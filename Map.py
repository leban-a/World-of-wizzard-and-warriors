from Scene import*

class Map():
    scenes = {
    'Scene':Scene(),
    'Intro Setup':Intro_Setup(),
    #'Choose Character': Choose_Character(),
    'Intro World Opening':Intro_World_Opening(),
    'Talihu':Talihu()
    }
    def __init__(self, start_scene):
        self.start_scene = start_scene


    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
