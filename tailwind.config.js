/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ["src/frontend/**/*.js", "src/frontend/**/*.html"],
    theme: {
        extend: {
            colors: {
                primary: "#d68367",
                dark: {
                    DEFAULT: "#11151c",
                    100: "#151b25",
                    200: "#222c3d",
                    300: "#384150",
                    400: "#536696",
                },
            },
        },
    },
    plugins: [],
};
