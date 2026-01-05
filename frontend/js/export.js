
let previewData = [];

async function loadPreview(){
  const res = await fetch("http://127.0.0.1:5000/export-preview");
  const data = await res.json();

  previewData = data;

  const body = document.getElementById("previewBody");
  body.innerHTML = "";

  data.forEach(item => {
    const dt = new Date(item.createdAt);
    const tr = document.createElement("tr");

    tr.innerHTML = `
      <td>${item.memberName}</td>
      <td>₹${item.amount}</td>
      <td>${dt.toLocaleDateString()}</td>
      <td>${dt.toLocaleTimeString()}</td>
      <td>${item.requestId || ""}</td>
    `;

    body.appendChild(tr);
  });
}

function exportData(){
  if(previewData.length === 0){
    alert("No data to export");
    return;
  }

  let csv = "Member,Amount,Date,Time,Request ID\n";

  previewData.forEach(item => {
    const dt = new Date(item.createdAt);
    csv += `${item.memberName},${item.amount},${dt.toLocaleDateString()},${dt.toLocaleTimeString()},${item.requestId || ""}\n`;
  });

  const blob = new Blob([csv], { type: "text/csv;charset=utf-8;" });
  const url = URL.createObjectURL(blob);

  const a = document.createElement("a");
  a.href = url;
  a.download = "expenses.csv";
  a.click();
}

function goBack(){
  window.location.href = "member-home.html";
}

loadPreview();
