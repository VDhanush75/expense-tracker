

async function loadStatus(){

  const memberName = document.getElementById("memberSelect").value;

  if(!memberName){
    alert("Please select a member");
    return;
  }

  const res = await fetch(`http://127.0.0.1:5000/member-requests?memberName=${memberName}`);

  if(!res.ok){
    console.error(await res.text());
    return;
  }

  const data = await res.json();

  const box = document.getElementById("statusList");
  box.innerHTML = "";

  data.forEach(req => {
    const card = document.createElement("div");
    card.className = "status-card";
    card.innerHTML = `
      <b>${req.memberName}</b>
      <p>₹${req.amount} — ${req.reason}</p>
      <span class="status ${req.status}">${req.status}</span>
    `;
    box.appendChild(card);
  });
}
function goHome(){
  window.location.href = "member-home.html";
}