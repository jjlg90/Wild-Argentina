//This function provides backend email services to the contact form
function sendMail(contactForm) {
    emailjs.send("wildArgentinaID","wildArgentina", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "message": contactForm.message.value
    })
        .then(
            function (response) {
                console.log("SUCCESS", response);
                document.getElementById("modal2trigger").click();
                $('#modal2content').html("SUCCESS!<br/>Message has been sent.")
                document.getElementById("contact-form").reset();
                document.getElementById("close").click();
            },
            function (error) {
                console.log("FAILED", error);
                document.getElementById("modal2trigger").click();
                $('#modal2content').html("Woops! It seems we have run into some issues<br/>please try again in a few minutes");
            }
        );
    return false; // To block from loading a new page
}