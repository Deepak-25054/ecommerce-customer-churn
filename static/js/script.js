document
    .getElementById("predictionForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);

        const resultDiv = document.getElementById("result");
        const predictButton = document.getElementById("predictButton");

        predictButton.disabled = true;
        predictButton.textContent = "Analyzing...";

        resultDiv.innerHTML = `
            <div class="result-placeholder">
                <div class="result-icon">...</div>
                <h3>Analyzing Customer</h3>
                <p>Please wait while the ML model processes the data.</p>
            </div>
        `;

        try {

            const response = await fetch("/predict", {
                method: "POST",
                body: formData
            });

            const data = await response.json();

            if (!response.ok || data.error) {
                throw new Error(data.error || "Prediction failed.");
            }

            const isChurn = data.prediction === 1;

            const statusClass = isChurn
                ? "status-risk"
                : "status-safe";

            const statusText = isChurn
                ? "Churn Risk Detected"
                : "Low Churn Risk";

            resultDiv.innerHTML = `
                <div class="prediction-result">

                    <div class="result-status ${statusClass}">
                        ${statusText}
                    </div>

                    <h3>${data.result}</h3>

                    <p class="probability">
                        Churn Probability:
                        <strong>${data.probability}%</strong>
                    </p>

                </div>
            `;

        } catch (error) {

            resultDiv.innerHTML = `
                <div class="error">
                    ${error.message}
                </div>
            `;

            console.error(error);

        } finally {

            predictButton.disabled = false;
            predictButton.textContent = "Predict Customer Churn";
        }
    });