# Copyright (c) 2025, Jecintha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import now

class ServiceBooking(Document):
	def validate(self):
		if self.status == "Requested" and self.preferred_datetime < now():	
			frappe.throw("Preferred Date/Time can't be paste.")
	
	def on_update(self):
		if self.status == "Approved":
			self.send_confirmation_email()
   
	def send_confirmation_email(self):
		try:
			dt = datetime.strptime(str(self.preferred_datetime), "%Y-%m-%d %H:%M:%S")
			email_template = frappe.get_doc("Email Template","Service Booking")
			data = {
				"customer_name":self.customer_name,
				"booking_date":dt.date().strftime("%Y-%m-%d"),
				"booking_time":dt.time().strftime("%I:%M %p"),
				"service_type":self.service_type
			}
			subject = "Spa Booking Confirmation"
			message = frappe.render_template(email_template.response,data)
			frappe.sendmail(
				recipients=[self.customer_email],
				subject=subject,
				message=message
			)
		except Exception:
			frappe.throw("Email notification sent failed to customer..!")
   
   
   
   
