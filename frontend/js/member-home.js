const members = ["Family","Dad","Mom","Nikhil","Suma","Durga","Dhanush","Varu"];

async function loadDashboard(){
  const res = await fetch("http://127.0.0.1:5000/all-expenses");
  const expenses = await res.json();

  let total = 0;
  const map = {};
  members.forEach(m => map[m] = 0);

  expenses.forEach(e => {
    total += Number(e.amount);
    if(map[e.memberName] !== undefined){
      map[e.memberName] += Number(e.amount);
    }
  });

  document.getElementById("totalExpense").textContent = "₹" + total;

  const grid = document.getElementById("memberCards");
  grid.innerHTML = "";

  members.forEach(name => {
    const card = document.createElement("div");
    card.className = "member-card";
    card.innerHTML = `<b>${name}</b><span>₹${map[name]}</span>`;
    grid.appendChild(card);
  });
}

function toggleSidebar(){
  document.getElementById("sidebar").classList.toggle("active");
}
function goMemberHome(){ location.href="member-home.html"; }



function goPage(p){ window.location.href = p; }
function logout(){
  localStorage.clear();
  window.location.href = "login.html";
}

loadDashboard();
