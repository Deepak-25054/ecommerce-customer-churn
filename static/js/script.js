document
    .getElementById("predictionForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);

        const resultDiv = document.getElementById("result");

        resultDiv.innerHTML = "Predicting...";

        try {

            const response = await fetch("/predict", {
                method: "POST",
                body: formData
            });

            const data = await response.json();

            if (data.error) {
                resultDiv.innerHTML =
                    `<p class="error">Error: ${data.error}</p>`;
                return;
            }

            resultDiv.innerHTML = `
                <h2>${data.result}</h2>
                <p>Churn Probability: <strong>${data.probability}%</strong></p>
            `;

        } catch (error) {

            resultDiv.innerHTML =
                `<p class="error">Unable to connect to the server.</p>`;

            console.error(error);
        }
    });