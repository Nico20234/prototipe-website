
document.addEventListener("DOMContentLoaded", function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-button');
    const cartContainer = document.getElementById('cart');
    
    addToCartButtons.forEach(button => {
        button.addEventListener('click', function() {
            const item = button.getAttribute('data-item');
            const cartItem = document.createElement('div');
            cartItem.textContent = item;
            cartContainer.appendChild(cartItem);
        });
    });
}); 


/*
<script>
const URL = "http://127.0.0.1/5000"

//const URL = "https://USUARIO.pythonanywhere.com/"

// Capturamos el evento de envío del formulario
document.getElementById('formulario').addEventListener('submit', 
function (event) {
        event.preventDefault(); // Evitamos que se envie el form
        var formData = new FormData(this);
// Realizamos la solicitud POST al servidor
        fetch(URL + 'usuarios', {
        method: 'POST',
        body: formData 
    })

    .then(function (response) {
            if (response.ok) {
                return response.json();
            } else {
                throw new Error('Error al registrar el Usuario.');}
    })


    .then(function (data) {
        alert('Usuario registrado correctamente.');
    })

    .catch(function (error) {
        alert('Error al registrar el Usuario.');
    })

    .finally(function () {
        document.getElementById('email').value = "";
        document.getElementById('password').value = "";
    });
})
</script>
*/