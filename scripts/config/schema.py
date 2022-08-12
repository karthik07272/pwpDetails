class schema:
    user_type={
        6:"Brand Owners",
        7:"Producers",
        8:"Importers"
    }
    header_contents=[
        {
            "label": "Category",
            "value": "category"
        },
        {
            "label": "Received",
            "value":"received"
        },
        {
            "label": "InProcess",
            "value": "inProgress"
        },
        {
            "label": "NotApproved",
            "value": "notApproved"
        },
        {
            "label": "RegistrationIssued",
            "value": "registrationIssued"
        },
        {
            "label": "Total Received",
            "value": "totalReceived"
        }
    ]


    breadCrumbItems =[
            {
                "key": "home",
                "label": "Home",
                "route": "epr/dashboard"
            },
            {
                "key": "profile",
                "label": "Profile",
                "route": "epr/profile"
            }
        ]
    tabSet= [
        {
            "key": "companyDetails",
            "label": "Company Details"
        },
        {
            "key": "authorizedPerson",
            "label": "Authorized person"
        },
        {
            "key": "PWPDetails",
            "label": "PWP details"
        }
    ]

    companyDetails= [
        {
            "key": "companyName",
            "label": "Name"
        },
        {
            "key": "registeredAddress",
            "label": "Registered Address"
        },
        {
            "key": "state",
            "label": "State"
        },
        {
            "key": "district",
            "label": "District"
        },
        {
            "key": "pinCode",
            "label": "Pin code"
        },
        {
            "key": "type",
            "label": "Type of Plastic Waste Processor"
        }
    ]

    authorizedPerson= [
        {
            "key": "authorizedPersonName",
            "label": "Name"
        },
        {
            "key": "designation",
            "label": "Designation"
        },
        {
            "key": "mobile",
            "label": "Mobile No"
        },
        {
            "key": "authorizedPersonPAN",
            "label": "PAN No."
        },
        {
            "key": "Aadhaar",
            "label": "Aadhaar No."
        },
        {
            "key": "email",
            "label": "Email Id"
        }
    ]

    PWPDetails= [
        {
            "key": "GST",
            "label": "GST No."
        },
        {
            "key": "PWPDetailsPAN",
            "label": "PAN Number"
        },
        {
            "key": "CIN",
            "label": "CIN"
        }
    ]

