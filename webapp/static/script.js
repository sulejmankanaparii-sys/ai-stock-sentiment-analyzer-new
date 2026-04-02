document.getElementById("analyze-form").addEventListener("submit", async (e) => {
    e.preventDefault();

    const ticker = document.getElementById("ticker").value;
    const source = document.getElementById("source").value;
    const start_date = document.getElementById("start_date").value;
    const end_date = document.getElementById("end_date").value;

    if (source === "api" && (!start_date || !end_date)) {
        alert("Please select start and end dates for API");
        return;
    }

    const response = await fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            ticker,
            source,
            start_date,
            end_date
        })
    });


    const data = await response.json();

    console.log(data); // debug

    const signal = data.signal || "neutral";

    const signalClass =
        signal.toLowerCase() === "bullish" ? "bullish" :
        signal.toLowerCase() === "bearish" ? "bearish" :
        "neutral";

    document.getElementById("results").innerHTML = `
        <h2>${data.ticker} Analysis</h2>

        <p class="signal ${signalClass}">
            Signal: ${signal}
        </p>

        <p><strong>Sentiment Score:</strong> ${Number(data.sentiment_score).toFixed(3)}</p>
        <p><strong>Articles:</strong> ${data.articles}</p>

        ${data.chart_path ? `<img src="${data.chart_path}" />` : ""}
    `;
});