import math
import random
from panda3d.core import NodePath, Point3, VBase4, TextNode, Vec3, deg2Rad, CollisionSegment, CollisionHandlerQueue, CollisionNode, BitMask32
from panda3d.direct import SmoothMover
from direct.fsm import FSM
from direct.distributed import DistributedObject
from direct.distributed.ClockDelta import globalClockDelta
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import Sequence, ProjectileInterval, Parallel, LerpHprInterval, ActorInterval, Func, Wait, SoundInterval, LerpPosHprInterval, LerpScaleInterval
from direct.gui.DirectGui import DGG, DirectButton, DirectLabel, DirectWaitBar
from direct.task import Task
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.battle import MovieUtil
from direct.actor.Actor import Actor
from direct.interval.LerpInterval import LerpColorInterval
from direct.interval.LerpInterval import LerpScaleInterval

class DistributedNameDropperCabnit(DistributedObject.DistributedObject):
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        #Load The Cabnit!
        self.cr
        self.makeModel()
        
        self.accept("entercoll", self.giveReward)
        
        #Name Dropper Cabnits give Jellybeans! every once and a while you can also gain summons or fires.
    
    def makeModel(self):
        #Place Holder!
        
        self.cabND = Actor('phase_5/models/cogdominium/tt_namedropper_cabnit_zero.bam')
        self.cabND.reparentTo(render)
        self.cabND.setPos(-20, -20, 0)
    
    def giveReward(self, entry):
        print('Hi! here you go!')
        rewardMovie = LerpColorInterval(self.cabND, 0.3, Vec3(0, 0, 1), Vec3(1, 1, 1), blendType='easeInOut')
        rewardMovie2 = LerpColorInterval(self.cabND, 0.3, Vec3(1, 1, 1), Vec3(0, 0, 1), blendType='easeInOut')
        rewardScale = LerpScaleInterval(self.cabND, 0.3, Vec3(1, 1, 2), Vec3(1, 1, 1), blendType='easeInOut') 
        rewardScale2 = LerpScaleInterval(self.cabND, 0.3, Vec3(1, 1, 1), Vec3(1, 1, 2), blendType='easeInOut')
        gain = base.loader.loadSfx("phase_11/audio/sfx/LB_toonup.ogg")
        gain.play()
        rewardPlay = Sequence(rewardMovie, rewardMovie2).start()
        rewardPlay = Sequence(rewardScale, rewardScale2).start()
        self.sendUpdate("giveReward", [])