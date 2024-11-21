const baseConfig = {
    allowOutsideClick: true,
    scrollbarPadding: false,
    heightAuto: false,
    showClass: {
        popup: "swal2-show",
        backdrop: "swal2-backdrop-show",
        icon: "swal2-icon-show",
    },
    hideClass: {
        popup: "swal2-hide",
        backdrop: "swal2-backdrop-hide",
        icon: "swal2-icon-hide",
    },
    customClass: {
        container: "modal-open",
    },
};

if (typeof Swal !== "undefined") {
    Swal.mixin({
        scrollbarPadding: false,
        heightAuto: false,
    });
}

const SwalUtils = {
    success: function (message, title = "Sucesso") {
        return Swal.fire({
            ...baseConfig,
            icon: "success",
            title: title,
            text: message,
            confirmButtonColor: "#89e67e",
        });
    },

    error: function (message, title = "Erro") {
        return Swal.fire({
            ...baseConfig,
            icon: "error",
            title: title,
            text: message,
            confirmButtonColor: "#e66360",
        });
    },

    confirm: function (message, title = "Confirmação", confirmText = "Sim", cancelText = "Não") {
        return Swal.fire({
            ...baseConfig,
            icon: "question",
            title: title,
            text: message,
            showCancelButton: true,
            confirmButtonText: confirmText,
            cancelButtonText: cancelText,
            confirmButtonColor: "#6ea2eb",
            cancelButtonColor: "#666d74",
            reverseButtons: true,
        });
    },

    warning: function (message, title = "Atenção") {
        return Swal.fire({
            ...baseConfig,
            icon: "warning",
            title: title,
            text: message,
            confirmButtonColor: "#e6714b",
        });
    },

    toast: function (message, icon = "success", position = "top-end") {
        return Swal.fire({
            toast: true,
            position: position,
            icon: icon,
            title: message,
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
            showClass: {
                popup: "swal2-show",
                backdrop: "swal2-backdrop-show",
            },
            hideClass: {
                popup: "swal2-hide",
                backdrop: "swal2-backdrop-hide",
            },
        });
    },

    loading: function (message = "Carregando...") {
        return Swal.fire({
            ...baseConfig,
            title: message,
            allowOutsideClick: false,
            showConfirmButton: false,
            willOpen: function () {
                Swal.showLoading();
            },
        });
    },

    prompt: function (message, title = "Digite", inputPlaceholder = "") {
        return Swal.fire({
            ...baseConfig,
            title: title,
            text: message,
            input: "text",
            inputPlaceholder: inputPlaceholder,
            showCancelButton: true,
            confirmButtonText: "OK",
            cancelButtonText: "Cancelar",
            inputValidator: function (value) {
                if (!value) {
                    return "Você precisa escrever algo!";
                }
            },
        });
    },

    html: function (htmlContent, title = "") {
        return Swal.fire({
            ...baseConfig,
            title: title,
            html: htmlContent,
            confirmButtonText: "OK",
        });
    },

    delete: function (message = "Esta ação não poderá ser revertida!", title = "Tem certeza?") {
        return Swal.fire({
            ...baseConfig,
            title: title,
            text: message,
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#e66360",
            cancelButtonColor: "#666d74",
            confirmButtonText: "Sim, deletar!",
            cancelButtonText: "Cancelar",
        });
    },

    autoClose: function (message, title = "", timer = 2000) {
        return Swal.fire({
            ...baseConfig,
            title: title,
            text: message,
            timer: timer,
            timerProgressBar: true,
            showConfirmButton: false,
        });
    },
};
