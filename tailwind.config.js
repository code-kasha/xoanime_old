/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "templates/*.html",
    "templates/**/*.html",
    "templates/**/**/*.html",
    "templates/**/**/**/*.html",
    "templates/**/**/**/**/*.html.html",
    "node_modules/flowbite/dist/*.min.js",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("flowbite/plugin"), require("tailwind-scrollbar")],
}
