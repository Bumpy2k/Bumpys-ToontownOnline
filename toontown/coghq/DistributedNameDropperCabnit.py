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

class DistributedNameDropperCabnit(DistributedObject.DistributedObject):
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        #Load The Cabnit!
        self.makeModel()
        
        #Name Dropper Cabnits give Jellybeans! every once and a while you can also gain summons or fires.
    
    def makeModel(self):
        #Place Holder!
        cabnit = loader.loadModel('phase_5/models/cogdominium/tt_m_ara_cmg_cabinetSmFalling.bam')
        cabnit.reparentTo(render)