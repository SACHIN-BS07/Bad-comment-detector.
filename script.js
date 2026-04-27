async function checkComment() {
    const text = document.getElementById("comment").value;

    if (!text) {
        alert("Please enter a comment!");
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: text })
        });

        const data = await response.json();

        document.getElementById("result").innerHTML =
            `Result: ${data.result} <br> Confidence: ${data.confidence}%`;

    } catch (error) {
        document.getElementById("result").innerHTML =
            "❌ Error connecting to backend!";
        console.error(error);
    }
}