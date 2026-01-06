
document.getElementById("requestForm").addEventListener("submit", async e => {
  e.preventDefault();

  const memberName = document.getElementById("memberName").value;
  const amount = document.getElementById("amount").value;
  const reason = document.getElementById("reason").value;

  try {
    const res = await fetch("https://expense-tracker-53vr.onrender.com/add-request", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ memberName, amount, reason })
    });

    const data = await res.json();
    console.log("SERVER RESPONSE:", data);



if(data.status === "insufficient"){
  alert("❌ Insufficient Fund");
  return;
}

if(!data.success){
  alert("❌ Server error. Try again.");
  return;
}

alert("✅ Request sent successfully");
document.getElementById("requestForm").reset();

  } catch (err) {
    console.error("REQUEST ERROR:", err);
    alert("❌ Server not responding");
  }
});

function goHome(){
  window.location.href = "member-home.html";
}
