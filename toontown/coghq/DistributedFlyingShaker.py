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
from toontown.suit import Suit, DistributedSuitBase
from toontown.suit import SuitDNA
from toontown.battle import BattleProps

class DistributedFlyingShaker(DistributedObject.DistributedObject):
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.cr = cr
        self.moverDudes()
    
    def moverDudes(self):
        shaker = DistributedSuitBase.DistributedSuitBase(self.cr)
        shakerDNA = SuitDNA.SuitDNA()
        shakerDNA.newSuit('ms')
        shaker.setDNA(shakerDNA)
        shaker.setDisplayName('Mover & Shaker')
        shaker.setPickable(0)
        shaker.reparentTo(render)
        shaker.doId = 0
        shaker.initializeBodyCollisions('toon')
        shaker.setPos(-10, -20, 10)
        self.prop = BattleProps.globalPropPool.getProp('propeller')
        head = shaker.find('**/joint_head')
        self.prop.reparentTo(head)
        shaker.setBlend(frameBlend=True)
        self.prop.setBlend(frameBlend=True)
        self.propTrack = Sequence(ActorInterval(self.prop, 'propeller', startFrame=0, endFrame=14)).loop()
        self.hoverSeq = Sequence(ActorInterval(shaker, 'landing', startFrame=10, endFrame=20, playRate=0.5), ActorInterval(shaker, 'landing', startFrame=20, endFrame=10, playRate=0.5)).loop()
        pathPoints = [Vec3(-80, -60, 10),
         Vec3(-40, -40, 10),
         Vec3(-10, -20, 15),
         Vec3(-50, -25, 5),
         Vec3(-80, -60, 10)]
        self.tutWalkTrack = shaker.makePathTrack(shaker, pathPoints, 6, 'moveShaker').loop()