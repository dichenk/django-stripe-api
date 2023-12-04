document.getElementById('buy-button').addEventListener('click', function() {
    const itemId = this.dataset.itemId;
    const quantity = document.getElementById('quantity').value;

    fetch('/buy/stripe-key')
        .then(response => response.json())
        .then(keyData => {
            const stripe = Stripe(keyData.stripePublicKey);

            fetch(`/buy/${itemId}?quantity=${quantity}`)
                .then(response => response.json())
                .then(data => {
                    stripe.redirectToCheckout({ sessionId: data.sessionId });
                })
                .catch(error => console.error('Error:', error));
        })
        .catch(error => console.error('Error fetching Stripe key:', error));
});