from fastapi import APIRouter
from scripts.core.models import candidate_model
from scripts.core.handlers.user_management_handler import UserManagement
from scripts.logging.application_logging import logger
from scripts.config.app_constants import *
router = APIRouter()
router1 = APIRouter(prefix=Routes.manage_users)
router2 = APIRouter(prefix=Routes1.pwp_details)


class output:
    @staticmethod
    @router1.post(ManageUser.insertUser, tags=[Routes.manage_users])
    async def dashboard_statistics(input_json:candidate_model.states):
        try:
            return UserManagement().dashboard_statistics(input_json)
        except Exception as e:
            logger.error("Exception while fetching data  ----> " + str(e))
            return {"status": "failed", "message": "failed"}

    @staticmethod
    @router2.post(ManageUser1.insertUser1, tags=[Routes1.pwp_details])
    async def pwd_details(input_json:candidate_model.pwpDetail):
        try:
            return UserManagement().pwpDetails(input_json)
        except Exception as e:
            logger.error("Exception while fetching data  ----> " + str(e))
            return {"status": "failed", "message": "failed"}