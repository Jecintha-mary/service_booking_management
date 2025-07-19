import frappe

@frappe.whitelist(methods=["POST"], allow_guest=True)
def send_booking_details():
    try:
        customer = frappe.form_dict.get("customer")
        page = int(frappe.form_dict.get("page", 1)) 
        page_length = 20
        page_start = (page - 1) * page_length
        if not customer:
            frappe.local.response["message"] = "Missing customer."
            frappe.local.response["http_status_code"] = 400
            return
        total = frappe.db.count("Service Booking", filters = {"customer": customer})
        if total:
            booking_details = frappe.get_all(
                "Service Booking",
                filters = {"customer": customer},
                fields = [
                    "name", "customer", "service_type",
                    "preferred_datetime", "customer_name",
                    "customer_email", "status"
                ],
                start = page_start,
                page_length = page_length
            )
            frappe.local.response["message"] = {
                            "results": booking_details,
                            "total": total,
                            "page": page,
                            "page_length": page_length
                        }
            frappe.local.response["http_status_code"] = 200
        else:
            frappe.local.response["message"] = "No booking details found."
            frappe.local.response["http_status_code"] = 404
    except Exception as e:
        frappe.log_error(title="send_booking_details", message=frappe.get_traceback())
        frappe.local.response["message"] = "Something went wrong."
        frappe.local.response["http_status_code"] = 500