from aiogram import Bot, Dispatcher
from ITPHelper.Utils.Logger import Logger
import ITPHelper.Utils.Config as Config
<<<<<<< HEAD
<<<<<<< HEAD

from ITPHelper.Core.Assignments import AssignmentsManager, CodeManager
=======
>>>>>>> parent of 128b3d6 (feat: AssignmentsManager added)
=======
>>>>>>> parent of 128b3d6 (feat: AssignmentsManager added)


class ITPHelperBot(Bot):
    def __init__(self):
        super().__init__(token=Config.token)


instance = ITPHelperBot()
dp = Dispatcher()
logger = Logger("log.txt")
<<<<<<< HEAD
<<<<<<< HEAD

assignmentsManager = AssignmentsManager()
codeManager = CodeManager()
=======
>>>>>>> parent of 128b3d6 (feat: AssignmentsManager added)
=======
>>>>>>> parent of 128b3d6 (feat: AssignmentsManager added)
