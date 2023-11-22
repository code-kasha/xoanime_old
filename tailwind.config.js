/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "templates/*.html",
    "templates/**/*.html",
    "templates/**/**/*.html",
    "templates/**/**/**/*.html",
    "templates/**/**/**/**/*.html",
    "node_modules/flowbite/dist/*.min.js",
  ],
  theme: {
    extend: {
      screens: {
        gf: "280px", // Galaxy Fold (Shortest usable screen size)
        mb: "320px", // Normal mobile
        xxs: "400px", // Large mobile (e.g., iPhone 6/7/8)
        xs: "480px", // Extra-small tablets and large phones
        sm: "600px", // Small tablets
        md: "768px", // Tablet (e.g., iPad)
        lg: "1024px", // Small laptops
        xl: "1280px", // Larger laptops and desktops
        "2xl": "1440px", // Large desktops
        "3xl": "1536px", // Extra-large desktops
      },
    },
  },
  plugins: [require("flowbite/plugin"), require("tailwind-scrollbar")],
}
