function toggleMode() {
    var body = document.body;
    var modeButton = document.getElementById("switch");
  
    if (body.classList.contains("dark-mode")) {
      // 현재 다크 모드인 경우, 라이트 모드로 전환
      body.classList.remove("dark-mode");
      localStorage.setItem("mode", "light"); // 로컬 스토리지에 라이트 모드 상태 저장
    } else {
      // 현재 라이트 모드인 경우, 다크 모드로 전환
      body.classList.add("dark-mode");
      localStorage.setItem("mode", "dark"); // 로컬 스토리지에 다크 모드 상태 저장
    }
  }
  
  var modeButton = document.getElementById("switch");
  
  // 이전에 저장된 모드 상태를 가져와서 적용
  var savedMode = localStorage.getItem("mode");
  if (savedMode === "dark") {
    document.body.classList.add("dark-mode");
    modeButton.checked = true;
  } else {
    document.body.classList.remove("dark-mode");
    modeButton.checked = false;
  }
  
  modeButton.addEventListener("change", toggleMode);