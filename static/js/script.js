document
    .getElementById("predictionForm")
    .addEventListener("submit", async function (event) {

        event.preventDefault();

        const form = event.target;
        const formData = new FormData(form);

        const resultDiv =
            document.getElementById("result");

        const predictButton =
            document.getElementById("predictButton");


        // ==================================================
        // LOADING STATE
        // ==================================================

        predictButton.disabled = true;

        predictButton.innerHTML = `
            <span>Analyzing Customer...</span>
        `;


        resultDiv.innerHTML = `
            <div class="result-loading">

                <div class="loading-spinner"></div>

                <h3>
                    Analyzing Customer
                </h3>

                <p>
                    XGBoost is evaluating the customer information.
                </p>

            </div>
        `;


        try {

            // ==================================================
            // SEND DATA TO FLASK
            // ==================================================

            const response = await fetch("/predict", {
                method: "POST",
                body: formData
            });


            // ==================================================
            // READ RESPONSE
            // ==================================================

            const responseText =
                await response.text();


            console.log(
                "Server response:",
                responseText
            );


            let data;

            try {

                data = JSON.parse(responseText);

            } catch (parseError) {

                console.error(
                    "JSON parsing error:",
                    parseError
                );

                throw new Error(
                    "Server returned an unexpected response."
                );

            }


            // ==================================================
            // HANDLE BACKEND ERROR
            // ==================================================

            if (!response.ok || data.error) {

                throw new Error(
                    data.error ||
                    "Prediction failed."
                );

            }


            // ==================================================
            // GET PREDICTION DATA
            // ==================================================

            const probability =
                Number(data.probability);

            const isChurn =
                data.prediction === 1;


            // ==================================================
            // DETERMINE RISK LEVEL
            // ==================================================

            let riskLevel;
            let riskDescription;
            let riskClass;


            if (probability >= 70) {

                riskLevel = "High Risk";

                riskDescription =
                    "This customer shows a high probability of churn.";

                riskClass = "risk-high";

            }

            else if (probability >= 40) {

                riskLevel = "Medium Risk";

                riskDescription =
                    "This customer shows a moderate probability of churn.";

                riskClass = "risk-medium";

            }

            else {

                riskLevel = "Low Risk";

                riskDescription =
                    "This customer currently shows a low probability of churn.";

                riskClass = "risk-low";

            }


            // ==================================================
            // SAVE REPORT DATA
            // ==================================================

            const reportData = {

                // Customer information

                customer: {

                    Tenure:
                        formData.get("Tenure"),

                    WarehouseToHome:
                        formData.get("WarehouseToHome"),

                    NumberOfDeviceRegistered:
                        formData.get(
                            "NumberOfDeviceRegistered"
                        ),

                    PreferredOrderCat:
                        formData.get(
                            "PreferredOrderCat"
                        ),

                    SatisfactionScore:
                        formData.get(
                            "SatisfactionScore"
                        ),

                    MaritalStatus:
                        formData.get(
                            "MaritalStatus"
                        ),

                    NumberOfAddress:
                        formData.get(
                            "NumberOfAddress"
                        ),

                    Complain:
                        formData.get("Complain"),

                    DaySinceLastOrder:
                        formData.get(
                            "DaySinceLastOrder"
                        ),

                    CashbackAmount:
                        formData.get(
                            "CashbackAmount"
                        )

                },


                // Prediction information

                prediction: {

                    value:
                        Number(data.prediction),

                    result:
                        data.result,

                    probability:
                        probability,

                    riskLevel:
                        riskLevel,

                    riskDescription:
                        riskDescription

                }

            };


            // Store report in browser session

            sessionStorage.setItem(
                "churnReport",
                JSON.stringify(reportData)
            );


            console.log(
                "Prediction report saved:",
                reportData
            );


            // ==================================================
            // STATUS
            // ==================================================

            const statusClass =
                isChurn
                    ? "status-risk"
                    : "status-safe";


            const statusText =
                isChurn
                    ? "Churn Risk Detected"
                    : "Low Churn Risk";


            // ==================================================
            // DISPLAY RESULT
            // ==================================================

            resultDiv.innerHTML = `

                <div class="advanced-result">


                    <!-- Status -->

                    <div class="result-status ${statusClass}">
                        ${statusText}
                    </div>


                    <!-- Probability -->

                    <div class="probability-display">

                        <div class="probability-value">
                            ${probability.toFixed(2)}%
                        </div>

                        <div class="probability-label">
                            Churn Probability
                        </div>

                    </div>


                    <!-- Probability Meter -->

                    <div class="probability-meter">

                        <div
                            class="probability-fill ${riskClass}"
                            style="width: ${probability}%;">
                        </div>

                    </div>


                    <!-- Risk Summary -->

                    <div class="risk-summary ${riskClass}">

                        <div class="risk-title">

                            <span class="risk-indicator"></span>

                            ${riskLevel}

                        </div>

                        <p>
                            ${riskDescription}
                        </p>

                    </div>


                    <!-- Prediction -->

                    <div class="prediction-message">

                        <strong>
                            ${data.result}
                        </strong>

                        <span>
                            XGBoost model prediction
                        </span>

                    </div>


                    <!-- Detailed Report -->

                    <a
                        href="/result"
                        class="report-view-button">

                        View Detailed Report →

                    </a>


                    <!-- Reset -->

                    <button
                        type="button"
                        class="reset-button"
                        onclick="resetPrediction()">

                        Analyze Another Customer

                    </button>


                </div>

            `;


        } catch (error) {

            console.error(
                "Prediction error:",
                error
            );


            resultDiv.innerHTML = `

                <div class="error">

                    <strong>
                        Prediction Error
                    </strong>

                    <p>
                        ${error.message}
                    </p>

                </div>

            `;

        }


        finally {

            predictButton.disabled = false;

            predictButton.innerHTML = `

                <span>
                    Predict Customer Churn
                </span>

                <span class="button-arrow">
                    →
                </span>

            `;

        }

    });



/* =========================================================
   RESET PREDICTION
========================================================= */

function resetPrediction() {

    const resultDiv =
        document.getElementById("result");


    // Remove previous report

    sessionStorage.removeItem(
        "churnReport"
    );


    resultDiv.innerHTML = `

        <div class="result-placeholder">

            <div class="result-icon">
                ?
            </div>

            <h3>
                Waiting for prediction
            </h3>

            <p>
                Enter customer information and click
                <strong>Predict Customer Churn</strong>.
            </p>

        </div>

    `;


    document
        .getElementById("predictionForm")
        .scrollIntoView({
            behavior: "smooth",
            block: "center"
        });

}