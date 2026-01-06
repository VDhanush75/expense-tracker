document.getElementById("loginBtn").addEventListener("click", async function () {

  const userId = document.getElementById("userId").value.trim();
  const password = document.getElementById("password").value.trim();
  const errorMsg = document.getElementById("errorMsg");

  errorMsg.textContent = "";

  if (!userId || !password) {
    errorMsg.textContent = "Please enter ID and Password";
    return;
  }

  try {
    const response = await fetch("https://expense-tracker-53vr.onrender.com/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ userId, password })
    });

    const data = await response.json();

if (data.success) {

  // Store logged-in user identity
  localStorage.setItem("loggedInUserId", data.name);
  localStorage.setItem("loggedInRole", data.role);

  // If member, store as currentMemberName for all member features
  if (data.role === "member") {
    // localStorage.setItem("currentMemberName", data.userId);
    localStorage.setItem("currentMemberName", data.name);
    console.log("LOGIN STORED MEMBER:", data.name);
    window.location.href = "member-home.html";
  }

  // If admin
  if (data.role === "admin") {
    window.location.href = "admin-analytics.html";
  }
}


  } catch (err) {
    errorMsg.textContent = "Server not responding";
    console.error(err);
  }
});
