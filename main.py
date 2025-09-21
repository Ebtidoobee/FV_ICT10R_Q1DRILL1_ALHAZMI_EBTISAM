from pyscript import document

def adding_numbers(event=None):
    if event:
        event.preventDefault()  # stop form reload

    try:
        # Get values from the input fields (default to 0 if empty)
        score1 = float(document.querySelector("#input1").value or 0)
        score2 = float(document.querySelector("#input2").value or 0)

        # Compute average
        avg = (score1 + score2) / 2

        # Output element
        output = document.querySelector("#output1")

        # Pass/Fail rule: 75+
        if avg >= 75:
            output.innerHTML = f"{avg:.2f} — Passed"
        else:
            output.innerHTML = f"{avg:.2f} — Failed"

    except:
        document.querySelector("#output1").innerHTML = "Error!"
