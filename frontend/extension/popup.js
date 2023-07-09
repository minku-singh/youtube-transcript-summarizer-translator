const btn = document.getElementById("summarise");
btn.addEventListener("click", function() {
    btn.disabled = true;
    btn.innerHTML = "Summarising...";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/summary?url=" + url, true);
        xhr.onload = function() {
            var text = xhr.responseText;
            const p = document.getElementById("output");
            p.innerHTML = text;
            btn.disabled = false;
            btn.innerHTML = "English";
        }
        xhr.send();
    });
});
const bdy = document.querySelector("body");
bdy.insertAdjacentHTML("afterend","<footer>")

const hindiBtn = document.getElementById("summariseHindi");
hindiBtn.addEventListener("click", function() {
    hindiBtn.disabled = true;
    hindiBtn.innerHTML = "Summarising...";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/summary-hindi?url=" + url, true);
        xhr.onload = function() {
            var text = xhr.responseText;
            const p = document.getElementById("output");
            p.innerHTML = text;
            hindiBtn.disabled = false;
            hindiBtn.innerHTML = "Hindi";
        }
        xhr.send();
    });
});

const marathiBtn = document.getElementById("summariseMarathi");
marathiBtn.addEventListener("click", function() {
    marathiBtn.disabled = true;
    marathiBtn.innerHTML = "Summarising...";
    chrome.tabs.query({currentWindow: true, active: true}, function(tabs){
        var url = tabs[0].url;
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "http://127.0.0.1:5000/summary-marathi?url=" + url, true);
        xhr.onload = function() {
            var text = xhr.responseText;
            const p = document.getElementById("output");
            p.innerHTML = text;
            marathiBtn.disabled = false;
            marathiBtn.innerHTML = "Marathi";
        }
        xhr.send();
    });
});