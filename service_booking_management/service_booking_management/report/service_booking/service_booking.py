# Copyright (c) 2025, Jecintha and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns, data = get_coloumns(filters), get_data(filters)
	return columns, data

def get_coloumns(filters):
    return [
        {
		"label":"Customer",
		"fieldname":"customer",
		"fieldtype":"Link",
		"options":"Customer Detail"
		},
		{
		"label":"Customer Name",
		"fieldname":"customer_name",
		"fieldtype":"Data"
		},	
		{
		"label":"Customer Email",
		"fieldname":"customer_email",
		"fieldtype":"Data"
		},	
  		{
		"label":"Service Type",
		"fieldname":"service_type",
		"fieldtype":"Data"
		},	
    	{
		"label":"Preferred Date/Time",
		"fieldname":"preferred_time",
		"fieldtype":"DateTime"
		},	
     	{
		"label":"Status",
		"fieldname":"status",
		"fieldtype":"Data"
		},	
 	]
    
def get_data(filters):
	condition = ""
	if filters.get("customer"):
		condition += """  AND SB.customer = '%s' """%filters.get("customer")
	if filters.get("service_type"):
		condition += """  AND SB.service_type = '%s' """%filters.get("service_type")
	if filters.get("status"):
		condition += """  AND SB.status = '%s' """%filters.get("status")
  
	data = frappe.db.sql(""" 
                      	SELECT 
							SB.customer,CD.full_name AS customer_name,CD.email AS customer_email,
							SB.service_type,SB.preferred_datetime AS preferred_time,SB.status
						FROM 
							`tabService Booking` SB INNER JOIN `tabCustomer Detail` CD ON SB.customer = CD.name
						WHERE
							1 = 1 {0}
                       
                       """.format(condition),as_dict = 1)
	return data