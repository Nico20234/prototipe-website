const contactForm = document.getElementById("contactForm");

contactForm.addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent default form submission

  const nameInput = document.getElementById("name");
  const emailInput = document.getElementById("email");
  const messageInput = document.getElementById("message");
  const reasonSelect = document.getElementById("reason");
  const subscribeCheckbox = document.getElementById("subscribe");

  let isValid = true;

  // Validate required fields
  if (nameInput.value.trim() === "") {
    alert("Please enter your name.");
    isValid = false;
  }
  if (emailInput.value.trim() === "") {
    alert("Please enter your email.");
    isValid = false;
  }
  if (messageInput.value.trim() === "") {
    alert("Please enter a message.");
    isValid = false;
  }
  if (reasonSelect.value === "") {
    alert("Please select a reason for contact.");
    isValid = false;
  }

  if (isValid) {
    // Form is valid, you can submit it here (e.g., using AJAX)
    alert("Form submitted successfully!");
    // contactForm.submit(); // Uncomment to submit the form if using traditional method
  }
});