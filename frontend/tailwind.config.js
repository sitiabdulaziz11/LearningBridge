/** @type {import('tailwindcss').Config} */
export default {

  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      margin: {
        'custom-sm': '13rem', // 160px
        'custom-lg': '20rem', // 256px
      }
    },
  },
  plugins: [],
  variants: {
    extend: {
      display: ["focus-group"],
  }
}
}
