// Copyright (c) 2025, Jecintha and contributors
// For license information, please see license.txt

frappe.query_reports["Service Booking"] = {
	"filters": [
		{
			"label":"Customer",
			"fieldname":"customer",
			"fieldtype":"Link",
			"options":"Customer Detail"
		},
		{
			"label":"Service Type",
			"fieldname":"service_type",
			"fieldtype":"Select",
			"options":["","Therapy","Spa","Others"],
			"default":"Therapy"
		},
		{
			"label":"Status",
			"fieldname":"status",
			"fieldtype":"Select",
			"options":["","Requested","Approved","Completed"],
			"default":"Approved"
		},
	]
};
