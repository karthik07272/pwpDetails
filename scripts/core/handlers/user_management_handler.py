import scripts
from scripts.logging.application_logging import logger
from scripts.utilities.mysql_utility import MYSQL_Utility
from scripts.config.schema import schema
class UserManagement:
    @staticmethod
    def dashboard_statistics(req_json):
        try:
            db = scripts.utilities.mysql_utility.MYSQL_Utility()
            stateName=req_json.state_name
            query = f"""SELECT * FROM company_business_type"""
            heading=stateName
            result = db.execute_query(query)
            true=True
            data_update=[]
            for each in result:
                body_content={'category':schema.user_type[each['user_type']],"Received": each['submitted'],"InProcess": each['inprocess'],
                              "NotApproved":each['rejected'],"RegistrationIssued":each['approved'],"totalReceived": each['submitted'] + each['inprocess'] + each['rejected'] + each['approved']
                              }
                data_update.append(body_content)

            response_output={
                "status":"success",
                "data":[
                    {
                        "heading":heading,
                        "tableActions": {},
                        "hideExternal": true,
                        "hideTableFooter": true,
                        "tableData":{
                            "headerContent": schema.header_contents,
                            "body_content":[data_update]
            }
                    }
                ]
            }
            return response_output
        except Exception as e:
            logger.error("Error while fetching the data" + str(e))
            raise Exception("Failed to fetching the data" + str(e))

    @staticmethod
    def pwpDetails(req_json=True):
        try:
            db = scripts.utilities.mysql_utility.MYSQL_Utility()
            query = f"""SELECT pwp_user_details_clone.company_name,pwp_user_details_clone.company_address,pwp_user_details_clone.company_pan,
            pwp_user_details_clone.user_pan,pwp_user_details_clone.state_id,pwp_user_details_clone.district, pwp_user_details_clone.pincode,
            pwp_user_details_clone.users_name,pwp_user_details_clone.designation,pwp_user_details_clone.mobile_no, pwp_user_details_clone.aadhaar,
            pwp_user_details_clone.email,pwp_user_details_clone.company_gst,pwp_user_details_clone.company_cin, processing_type.processing_type_name 
            FROM pwp_user_details_clone INNER JOIN processing_type ON pwp_user_details_clone.status=processing_type.status where email='rahul.krishnak@knowledgelens.com'""";
            result = db.execute_query(query)
            response_output = {
                "status": "success",
                "data": [
                    {
                        "breadCrumbItems":schema.breadCrumbItems,
                        "tabSet":schema.tabSet,
                        "activeTab":"companyDetails",
                        "visibleKeys": {
                            "companyDetails":schema.companyDetails,
                            "authorizedPerson":schema.authorizedPerson,
                            "PWPDetails":schema.PWPDetails
                                                },
                            "userDetails": result
                    }
                ]
            }
            return response_output
        except Exception as e:
            logger.error("Error while fetching the data" + str(e))