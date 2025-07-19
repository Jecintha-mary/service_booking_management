// Copyright (c) 2025, Jecintha and contributors
// For license information, please see license.txt

frappe.ui.form.on("Service Booking", {
	refresh(frm) {
        frm.events.make_readonly(frm)
	},
    make_readonly(frm){
        if(frm.doc.status != "Requested"){
            frm.disable_form();
        }
    }
});
