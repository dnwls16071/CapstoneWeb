function toggleMode() {
    var body = document.body;
    var modeButton = document.getElementById("switch");

    if (body.classList.contains("dark-mode")) {
        // 현재 다크 모드인 경우, 라이트 모드로 전환
        body.classList.remove("dark-mode");
    } else {
        // 현재 라이트 모드인 경우, 다크 모드로 전환
        body.classList.add("dark-mode");
    }
}

var modeButton = document.getElementById("switch");
modeButton.addEventListener("change", toggleMode);