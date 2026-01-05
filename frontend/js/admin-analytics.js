
async function loadAnalytics(){
  const res = await fetch("http://127.0.0.1:5000/analytics");
  const data = await res.json();

  document.getElementById("totalFund").textContent = "₹" + data.totalFund;
  document.getElementById("totalExpense").textContent = "₹" + data.totalExpense;
  document.getElementById("currentBalance").textContent = "₹" + data.currentBalance;

  buildMemberPie(data.memberMap);
  buildTrendBar(data.weekly, data.monthly, data.yearly);
}

function buildMemberPie(map){
  const labels = Object.keys(map);
  const values = Object.values(map);

  new Chart(document.getElementById("memberPie"), {
    type: "pie",
    data: {
      labels,
      datasets: [{
        data: values,
        backgroundColor: [
          "#ff6384","#36a2eb","#ffcd56","#4bc0c0",
          "#9966ff","#ff9f40","#8bc34a","#607d8b"
        ]
      }]
    },
    options:{
      plugins:{
        tooltip:{
          callbacks:{
            label: ctx => {
              const total = values.reduce((a,b)=>a+b,0);
              const percent = ((ctx.raw / total) * 100).toFixed(1);
              return `${ctx.label}: ₹${ctx.raw} (${percent}%)`;
            }
          }
        }
      }
    }
  });
}




function buildTrendBar(weekly, monthly, yearly){
  const labels = [
    ...Object.keys(weekly),
    ...Object.keys(monthly),
    ...Object.keys(yearly)
  ];

  const values = [
    ...Object.values(weekly),
    ...Object.values(monthly),
    ...Object.values(yearly)
  ];

  new Chart(document.getElementById("trendBar"), {
    type: "bar",
    data:{
      labels,
      datasets:[{
        label:"Expense Analytics",
        data: values,
        backgroundColor:"#3498db"
      }]
    },
    options:{
      plugins:{
        tooltip:{
          callbacks:{
            label: ctx => `₹${ctx.raw}`
          }
        }
      }
    }
  });
}




function toggleSidebar(){
  document.getElementById("sidebar").classList.toggle("active");
}

function goAnalytics(){ location.href="admin-analytics.html"; }
function goAddFund(){ location.href="admin-add-fund.html"; }
function goRequests(){ location.href="admin-requests.html"; }
function logout(){ location.href="login.html"; }

loadAnalytics();


