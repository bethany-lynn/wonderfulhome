// @type {import('tailwindcss').Config} 

module.exports = {
    purge: [
      './templates/**/*.html',
    ],
    theme: {
      extend: {
        fontFamily: {
          serif: ['Georgia', 'serif'],
          sans: ['Arial', 'sans'],
          monospace: ['Courier New', 'monospace'],
          cursive: ['Dancing Script', 'cursive'],
        },
      },
    },
    variants: {},
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
    ],
  };
  