document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const mobile = document.querySelector('input[name="mobile"]');
    const alternateMobile = document.querySelector('input[name="alternate_mobile"]');
    const pincode = document.querySelector('input[name="pincode"]');
    const budget = document.querySelector('input[name="budget"]');
    const fileInput = document.querySelector('input[name="project_complete_details"]');

    // Allow only numbers in mobile fields
    function allowOnlyNumbers(input, maxLength) {
        input.addEventListener("input", function () {
            this.value = this.value.replace(/\D/g, "").slice(0, maxLength);
        });
    }

    if (mobile) allowOnlyNumbers(mobile, 10);
    if (alternateMobile) allowOnlyNumbers(alternateMobile, 10);

    // Pincode validation
    if (pincode) {
        pincode.addEventListener("input", function () {
            this.value = this.value.replace(/\D/g, "").slice(0, 6);
        });
    }

    // Budget cannot be negative
    if (budget) {
        budget.addEventListener("input", function () {
            if (this.value < 0) {
                this.value = "";
            }
        });
    }

    // File validation
    if (fileInput) {
        fileInput.addEventListener("change", function () {

            const file = this.files[0];

            if (!file) return;

            const allowedTypes = [
                "application/pdf",
                "application/msword",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            ];

            const maxSize = 5 * 1024 * 1024; // 5 MB

            if (!allowedTypes.includes(file.type)) {
                alert("Only PDF, DOC, and DOCX files are allowed.");
                this.value = "";
                return;
            }

            if (file.size > maxSize) {
                alert("File size must be less than 5 MB.");
                this.value = "";
                return;
            }
        });
    }

    // Form submission validation
    form.addEventListener("client_submit", function (e) {

        const clientName = document.querySelector('input[name="client_name"]').value.trim();

        if (clientName === "") {
            alert("Client Name is required.");
            e.preventDefault();
            return;
        }

        if (mobile.value && mobile.value.length !== 10) {
            alert("Mobile Number must be 10 digits.");
            e.preventDefault();
            return;
        }

        if (
            alternateMobile.value &&
            alternateMobile.value.length !== 10
        ) {
            alert("Alternate Number must be 10 digits.");
            e.preventDefault();
            return;
        }

        if (
            pincode.value &&
            pincode.value.length !== 6
        ) {
            alert("Pincode must be 6 digits.");
            e.preventDefault();
            return;
        }

        alert("Client details validated successfully!");
    });

});