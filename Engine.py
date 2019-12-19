from Map import Map
from Loading import *


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        for scence in range(1,len(Map.scenes)):
            gap(),sec(0.5)
            gap(),sec(0.5)
            gap(),sec(0.5)
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        Map.scenes['Scene']



run_Map = Map("Intro Setup")
run_Game = Engine(run_Map)
run_Game.play()
