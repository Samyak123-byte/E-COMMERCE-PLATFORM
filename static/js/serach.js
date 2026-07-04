```javascript
// =====================================
// Product Search & Filter
// =====================================

document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("searchInput");
    const categoryFilter = document.getElementById("categoryFilter");
    const products = document.querySelectorAll(".product-card");
    const noResults = document.getElementById("noResults");

    function filterProducts() {

        const searchText = searchInput
            ? searchInput.value.toLowerCase().trim()
            : "";

        const selectedCategory = categoryFilter
            ? categoryFilter.value.toLowerCase()
            : "";

        let visibleProducts = 0;

        products.forEach(function (product) {

            const productName = product.dataset.name.toLowerCase();
            const productCategory = product.dataset.category.toLowerCase();

            const matchesSearch =
                productName.includes(searchText);

            const matchesCategory =
                selectedCategory === "" ||
                productCategory === selectedCategory;

            if (matchesSearch && matchesCategory) {

                product.style.display = "block";
                visibleProducts++;

            } else {

                product.style.display = "none";

            }

        });

        if (noResults) {

            noResults.style.display =
                visibleProducts === 0 ? "block" : "none";

        }

    }

    if (searchInput) {

        searchInput.addEventListener("keyup", filterProducts);

    }

    if (categoryFilter) {

        categoryFilter.addEventListener("change", filterProducts);

    }

    filterProducts();

});
```
