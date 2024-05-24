
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
