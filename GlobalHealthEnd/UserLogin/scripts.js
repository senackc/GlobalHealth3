
function login() {
    
    var form = document.forms["LoginForm"];
    var em = form.Identificicationnumber.value;
    var pw = form.Password.value;
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open('GET', 'https://reqres.in/api/users');
    xmlhttp.send()
    xmlhttp.onload = () => {
        console.log(xmlhttp.response);
        }
    // xmlhttp.open("post", "http://127.0.0.1:8000/user/login/", true);
    // xmlhttp.send({"Identificicationnumber":em,"Password":pw});
    // xmlhttp.open("get", "text.txt", true);
    
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            alert(this.responseText);
            
                
        }
    }
            
}


function loginResults(form) {
    var badLogin = document.getElementById("BadLogin");
    if (form.Email.value == "snc@gmail.com" && form.Password.value == "666") {
        badLogin.innerHTML = "Logged in as " + form.Email.value;
        badLogin.style.display = "block";
        //form.style.display = "none";
    } else {
        badLogin.style.display = "block";
        form.Email.select();
        form.Email.className = "Highlighted";
        setTimeout(function () {
            badLogin.style.display = 'none';
        }, 3000);
    }
}




document.getElementById("lgn").addEventListener("click", function () {
    var loginForm = document.getElementById("loginForm");
    login(loginForm);
});






function signup(signupForm) {
    var sem = signupForm.sEmail.value;
    var sun = signupForm.userName.value
    var spw = signupForm.sPassword.value;
    var xmlhttp = new XMLHttpRequest();
    //xmlhttp.open("post", "signup", true);
    var tmp = sem + sun + spw ;
    var blob = new Blob([tmp], { type: "text/plain;charset=utf-8" });
    var sFile = Storages.Binary("C:\\Users\\theca\\Desktop\\blabla\\text.txt");
    alert("slm");

    sFile.SaveAs("text.txt");
    //saveAs(blob,"text.txt");
       

        xmlhttp.onreadystatechange = function () {
            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                signupResults(signupForm);
            }
        }

}



document.getElementById("sgnUp").addEventListener("click", function () {
    var signForm = document.getElementById("signupForm");
    signup(signForm);
});




function signupResults(form) {
    
    alert("signed up as " + form.sEmail.value);

}