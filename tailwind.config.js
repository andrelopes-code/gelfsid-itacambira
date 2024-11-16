/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["src/frontend/**/*.js", "src/frontend/**/*.html"],
    theme: {
        extend: {
            colors: {
                primary: {
                    DEFAULT: "#d68367",
                    100: "#e4ac9b",
                },
                background: {
                    DEFAULT: "#f4f6f6",
                    100: "#f7faff",
                    200: "#ecf0f3",
                    400: "#485160",
                },
                dark: {
                    DEFAULT: "#11151c",
                    100: "#151b25",
                    200: "#222c3d",
                    400: "#536696",
                },
            },
        },
    },
    plugins: [],
};
