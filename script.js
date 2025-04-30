document.getElementById("loginForm").addEventListener("submit", function (e) {
    e.preventDefault();
    const username=document.getElementById("username").value;
    const password=document.getElementById("password").value;
    const message=document.getElementById("message");

    if(username === "ella123" && password ==="passwordku"){
       const welcome =document.createElement("p");
       welcome.id="welcome-message";
       welcome.textContent="Welcome, Ella!";
       document.querySelector(".login-container").appendChild(welcome);
    }
    
});