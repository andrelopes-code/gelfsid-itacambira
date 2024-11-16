async function select_directory() {
    result = await pywebview.api.select_directory();
    if (!result) return;

    const directoryDisplay = document.getElementById("directory-display");
    const directoryBtn = document.getElementById("directory-btn");

    directoryDisplay.textContent = result;
    directoryBtn.textContent = "PASTA SELECIONADA";
}
