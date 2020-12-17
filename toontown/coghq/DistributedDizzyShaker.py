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
from toontown.suit import Suit
from toontown.suit import SuitDNA

class DistributedDizzyShaker(DistributedObject.DistributedObject):
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.cr = cr
        self.moverDudes()
    
    def moverDudes(self):
        shaker = Suit.Suit()
        shaker.dna = SuitDNA.SuitDNA()
        shaker.dna.newSuit('ms')
        shaker.setDNA(shaker.dna)
        shaker.reparentTo(render)
        shaker.loop('lured')
        shaker.setPos(-20, -20, 0)
        self.stun = Actor('phase_3.5/models/props/stun-mod.bam', {'stun': 'phase_3.5/models/props/stun-chan.bam'})
        head = shaker.getHeadParts()[0]
        self.stun.reparentTo(head)
        self.stun.loop('stun')
        self.stun.setBlend(frameBlend=True)
        shaker.setBlend(frameBlend=True)