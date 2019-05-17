# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:48:37 2019

@author: Sammu
"""

import json
json_string="""
{    "student":{
   "first_name":"shamim",
   "last_name":"banu",
   "branch":"ece",
   "contact_no":[{"mobile_no":94686123,"phn_no":242301}]
   }
}"""
json_object=json.loads(json_string)
   
