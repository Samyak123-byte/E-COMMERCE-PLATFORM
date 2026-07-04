```javascript id="g7m2ka"
// ======================================
// Checkout JavaScript
// ======================================

document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("checkoutForm");

    if (!form) return;

    const submitBtn = document.getElementById("placeOrderBtn");

    form.addEventListener("submit", function (e) {

        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const phone = document.getElementById("phone").value.trim();
        const address = document.getElementById("address").value.trim();
        const city = document.getElementById("city").value.trim();
        const state = document.getElementById("state").value.trim();
        const zip = document.getElementById("zip").value.trim();
        const country = document.getElementById("country").value.trim();

        if (
            name === "" ||
            email === "" ||
            phone === "" ||
            address === "" ||
            city === "" ||
            state === "" ||
            zip === "" ||
            country === ""
        ) {

            e.preventDefault();

            alert("Please fill in all required fields.");

            return;

        }

        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        if (!emailPattern.test(email)) {

            e.preventDefault();

            alert("Please enter a valid email address.");

            return;

        }

        if (!confirm("Do you want to place this order?")) {

            e.preventDefault();

            return;

        }

        if (submitBtn) {

            submitBtn.disabled = true;

            submitBtn.innerHTML = "Processing...";

        }

    });

});
```
