/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "./app/templates/**/*.html",
    "./app/static/src/**/*.js",
    './node_modules/preline/dist/*.js',
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('preline/plugin'),
  ],
}