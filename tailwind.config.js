/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["src/frontend/**/*.js", "src/frontend/**/*.html"],
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: "#e6714b",
                },
                secondary: {
                    DEFAULT: "#666d74",
                },
                background: {
                    DEFAULT: "#f0f2f2",
                    lighter: "#f7faff",
                },
                border: {
                    DEFAULT: "#E7E5E5",
                },
            },
        },
    },
    plugins: [],
};
