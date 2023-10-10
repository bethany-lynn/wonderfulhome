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
      colors: {
        gray: {
          '1': '#5A5B5D',
          '2': '#38393B',
          '3': '#242526',
          '4': '#1A1B1C',
          '5': '#111212',
        },
      },
    },
    variants: {},
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
    ],
  };
  