const display = document.getElementById("display");
const buttons = document.querySelectorAll(".buttons button");

buttons.forEach(button => {
  button.addEventListener("click", event => {
    const buttonText = event.target.textContent;

    if (buttonText === "=") {
      try {
        display.value = eval(display.value);
      } catch (error) {
        display.value = "Error";
      }
    } else if (buttonText === "C") {
      display.value = "";
    } else {
      display.value += buttonText;
    }

    // Change cursor style while typing numbers
    if (!isNaN(buttonText) || buttonText === ".") {
      display.style.cursor = "text";
    } else {
      display.style.cursor = "pointer";
    }
  });
});
