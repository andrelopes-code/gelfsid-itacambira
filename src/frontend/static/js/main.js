let IMAGES_DIR = null;

async function select_directory() {
    result = await pywebview.api.files.select_directory();
    if (!result) return;

    const directoryDisplay = document.getElementById("directory-display");
    const directoryBtn = document.getElementById("directory-btn");

    IMAGES_DIR = result;
    directoryDisplay.textContent = result;
    directoryBtn.textContent = "PASTA SELECIONADA";
}

async function generate_pdf() {
    const data = document.getElementById("data-input").value;

    if (!IMAGES_DIR || !data) {
        SwalUtils.warning(
            "Você precisa informar o caminho para a pasta das imagens e também informar os dados copiados da planilha na caixa de texto!",
            "DADOS FALTANDO"
        );
        return;
    }

    result = await pywebview.api.pdf.generate(IMAGES_DIR, data);
}
