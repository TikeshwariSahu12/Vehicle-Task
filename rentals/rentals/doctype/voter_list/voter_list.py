# Copyright (c) 2024, Tikeshwari and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class VoterList(WebsiteGenerator):
	def validate(self):
		if (self.age < 18):
			frappe.throw("You are not eligible to vote..")
