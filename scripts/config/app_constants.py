class ResponseMessage:
    @staticmethod
    def final_res(status, data,heading, true):
        res = {"status": status, "data": data,"heading":heading, "tableActions": {}, "hideExternal": true,"hideTableFooter": true,}
        return res

class Message:
    success = "success"
    failure = "failure"

class Routes:
    manage_users = "/epr_prod"

class Routes1:
    pwp_details ="/profileDetails"

class ManageUser:
    insertUser = "/state_wise_details"

class ManageUser1:
    insertUser1 = "/pwpDetails"
