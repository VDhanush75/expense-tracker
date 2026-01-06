// Load all requests
async function loadRequests(){
  const res = await fetch("https://expense-tracker-53vr.onrender.com/admin-requests");
  const data = await res.json();

  const newBox = document.getElementById("newRequests");
  const historyBox = document.getElementById("historyRequests");

  newBox.innerHTML = "";
  historyBox.innerHTML = "";

  data.forEach(req => {

    // Skip admin self-requests
    if(req.memberName === "admin") return;

    const card = document.createElement("div");
    card.className = "card";

    card.innerHTML = `
      <b>${req.memberName}</b> — ₹${req.amount}<br>
      ${req.reason}<br>
      <small>Status: ${req.status}</small>
      <div class="actions"></div>
    `;

    const actions = card.querySelector(".actions");

    if(req.status === "pending"){
      actions.innerHTML = `
        <button onclick="handleAction('${req.requestId}','approve')">Approve</button>
        <button onclick="handleAction('${req.requestId}','reject')">Reject</button>
      `;
      newBox.appendChild(card);
    }
    else if(req.status === "approved"){
      actions.innerHTML = `
        <button onclick="handleAction('${req.requestId}','send')">Send</button>
      `;
      newBox.appendChild(card);
    }
    else{
      historyBox.appendChild(card);
    }

  });
}

// Button handler — must be global
async function handleAction(id, action){
  const res = await fetch("http://127.0.0.1:5000/update-request", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ requestId: id, action })
  });

  await res.json();
  loadRequests();
}

// Navigation
function goAnalytics(){
  window.location.href = "admin-analytics.html";
}

// Initial load
loadRequests();
