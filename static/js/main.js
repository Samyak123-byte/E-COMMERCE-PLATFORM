```javascript
// ======================================
// Flask E-Commerce Main JavaScript
// ======================================

document.addEventListener("DOMContentLoaded", function () {

    // ==============================
    // Auto Close Alerts
    // ==============================

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {

        setTimeout(function () {

            alert.classList.remove("show");
            alert.classList.add("fade");

            setTimeout(function () {
                alert.remove();
            }, 500);

        }, 3000);

    });

    // ==============================
    // Sticky Navbar
    // ==============================

    const navbar = document.querySelector(".navbar");

    if (navbar) {

        window.addEventListener("scroll", function () {

            if (window.scrollY > 20) {

                navbar.classList.add("shadow");

            } else {

                navbar.classList.remove("shadow");

            }

        });

    }

    // ==============================
    // Back To Top Button
    // ==============================

    const topBtn = document.getElementById("backToTop");

    if (topBtn) {

        window.addEventListener("scroll", function () {

            if (window.scrollY > 300) {

                topBtn.style.display = "block";

            } else {

                topBtn.style.display = "none";

            }

        });

        topBtn.addEventListener("click", function () {

            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });

        });

    }

    // ==============================
    // Product Search
    // ==============================

    const searchInput = document.getElementById("searchInput");

    if (searchInput) {

        searchInput.addEventListener("keyup", function () {

            const value = this.value.toLowerCase();

            document.querySelectorAll(".product-card").forEach(function (card) {

                const text = card.innerText.toLowerCase();

                card.style.display = text.includes(value) ? "" : "none";

            });

        });

    }

    // ==============================
    // Product Image Preview
    // ==============================

    const previewImage = document.getElementById("previewImage");

    const imageInput = document.getElementById("image");

    if (previewImage && imageInput) {

        imageInput.addEventListener("change", function () {

            if (!this.files.length) return;

            const reader = new FileReader();

            reader.onload = function (e) {

                previewImage.src = e.target.result;

            };

            reader.readAsDataURL(this.files[0]);

        });

    }

    // ==============================
    // Quantity Buttons
    // ==============================

    document.querySelectorAll(".increase-btn").forEach(function (button) {

        button.addEventListener("click", function () {

            const input = this.parentElement.querySelector(".quantity-input");

            if (input) {

                input.value = parseInt(input.value || 1) + 1;

            }

        });

    });

    document.querySelectorAll(".decrease-btn").forEach(function (button) {

        button.addEventListener("click", function () {

            const input = this.parentElement.querySelector(".quantity-input");

            if (input && parseInt(input.value) > 1) {

                input.value = parseInt(input.value) - 1;

            }

        });

    });

    // ==============================
    // Delete Confirmation
    // ==============================

    document.querySelectorAll(".delete-btn").forEach(function (button) {

        button.addEventListener("click", function (e) {

            if (!confirm("Are you sure you want to delete this item?")) {

                e.preventDefault();

            }

        });

    });

});
```
