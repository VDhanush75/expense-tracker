
document.getElementById("fundForm").onsubmit = async (e) => {
  e.preventDefault();

  const fundAmount = document.getElementById("amount").value;
  const fundReason = document.getElementById("reason").value;

  if(!fundAmount || !fundReason){
    alert("Please fill all fields");
    return;
  }

  await fetch("https://expense-tracker-53vr.onrender.com/add-fund", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ amount: fundAmount, reason: fundReason })
  });

  alert("Fund Added Successfully");
  e.target.reset();
};

// Navigation
function goBack(){
window.location.href="admin-analytics.html";
}

// Load Fund History
async function loadFundHistory(){
  const res = await fetch("https://expense-tracker-53vr.onrender.com/fund-history");
  const data = await res.json();

  const box = document.getElementById("fundHistory");
  box.innerHTML = "";

  data.forEach(fund => {
    const div = document.createElement("div");
    div.className = "history-card";
    div.innerHTML = `₹${fund.amount} — ${fund.reason} <small>${new Date(fund.createdAt).toLocaleString()}</small>`;
    box.appendChild(div);
  });
}

loadFundHistory();
