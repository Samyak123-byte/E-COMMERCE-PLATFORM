```javascript id="h3pf8m"
// =====================================
// Shopping Cart JavaScript
// =====================================

document.addEventListener("DOMContentLoaded", function () {

    const quantityInputs = document.querySelectorAll(".quantity-input");

    function updateCart() {

        let grandTotal = 0;

        quantityInputs.forEach(function (input) {

            const quantity = parseInt(input.value) || 1;
            const price = parseFloat(input.dataset.price);

            const subtotal = quantity * price;

            const row = input.closest("tr");

            if (row) {

                const subtotalCell = row.querySelector(".subtotal");

                if (subtotalCell) {
                    subtotalCell.innerText = "₹" + subtotal.toFixed(2);
                }

            }

            grandTotal += subtotal;

        });

        const totalElement = document.getElementById("grand-total");

        if (totalElement) {
            totalElement.innerText = "₹" + grandTotal.toFixed(2);
        }

    }

    quantityInputs.forEach(function (input) {

        input.addEventListener("input", function () {

            if (this.value < 1) {
                this.value = 1;
            }

            updateCart();

        });

    });

    // Increase Quantity

    document.querySelectorAll(".increase-btn").forEach(function (button) {

        button.addEventListener("click", function () {

            const input = this.parentElement.querySelector(".quantity-input");

            input.value = parseInt(input.value) + 1;

            updateCart();

        });

    });

    // Decrease Quantity

    document.querySelectorAll(".decrease-btn").forEach(function (button) {

        button.addEventListener("click", function () {

            const input = this.parentElement.querySelector(".quantity-input");

            if (parseInt(input.value) > 1) {

                input.value = parseInt(input.value) - 1;

            }

            updateCart();

        });

    });

    updateCart();

});
```
