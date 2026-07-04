```javascript id="z9r4hk"
// =====================================
// Admin Panel JavaScript
// =====================================

document.addEventListener("DOMContentLoaded", function () {

    // -------------------------
    // Auto Close Alerts
    // -------------------------

    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function(alert){

        setTimeout(function(){

            alert.classList.add("fade");

            setTimeout(function(){

                alert.remove();

            },500);

        },3000);

    });

    // -------------------------
    // Delete Confirmation
    // -------------------------

    const deleteButtons = document.querySelectorAll(".btn-danger");

    deleteButtons.forEach(function(button){

        button.addEventListener("click", function(e){

            if(!confirm("Are you sure you want to delete this item?")){

                e.preventDefault();

            }

        });

    });

    // -------------------------
    // Product Image Preview
    // -------------------------

    const imageInput = document.querySelector("input[type='file']");

    if(imageInput){

        imageInput.addEventListener("change", function(){

            const file = this.files[0];

            if(!file){
                return;
            }

            const reader = new FileReader();

            reader.onload = function(e){

                let preview = document.getElementById("previewImage");

                if(!preview){

                    preview = document.createElement("img");

                    preview.id = "previewImage";

                    preview.className = "img-thumbnail mt-3";

                    preview.style.maxWidth = "200px";

                    imageInput.parentNode.appendChild(preview);

                }

                preview.src = e.target.result;

            };

            reader.readAsDataURL(file);

        });

    }

    // -------------------------
    // Table Search
    // -------------------------

    const searchBox = document.getElementById("tableSearch");

    if(searchBox){

        searchBox.addEventListener("keyup", function(){

            const value = this.value.toLowerCase();

            const rows = document.querySelectorAll("tbody tr");

            rows.forEach(function(row){

                row.style.display =
                    row.innerText.toLowerCase().includes(value)
                    ? ""
                    : "none";

            });

        });

    }

    // -------------------------
    // Highlight Active Sidebar
    // -------------------------

    const current = window.location.pathname;

    document.querySelectorAll(".list-group-item").forEach(function(link){

        if(link.getAttribute("href") === current){

            link.classList.add("active");

        }

    });

    // -------------------------
    // Dashboard Counter Animation
    // -------------------------

    document.querySelectorAll(".dashboard-count").forEach(function(counter){

        const target = parseInt(counter.innerText);

        if(isNaN(target)){
            return;
        }

        let count = 0;

        const speed = Math.max(1, Math.ceil(target / 50));

        const timer = setInterval(function(){

            count += speed;

            if(count >= target){

                counter.innerText = target;

                clearInterval(timer);

            }
            else{

                counter.innerText = count;

            }

        },20);

    });

});
```
