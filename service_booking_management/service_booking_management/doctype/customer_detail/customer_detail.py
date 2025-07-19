# Copyright (c) 2025, Jecintha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from datetime import datetime


class CustomerDetail(Document):
	def validate(self):
		self.full_name = self.first_name if not self.first_name else f"{self.first_name} {self.last_name}"