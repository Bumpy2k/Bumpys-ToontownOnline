import random
from direct.distributed import DistributedObjectAI
from direct.fsm import FSM
from direct.directnotify import DirectNotifyGlobal
from toontown.coghq import BanquetTableBase
from toontown.toonbase import ToontownGlobals

class DistributedNameDropperCabnitAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedNameDropperCabnitAI')
    """
    
    The AI
    
    _____
    """
    def __init__(self, air, jbAmmount, fireAmmount, summonsAmount):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)

