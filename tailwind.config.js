/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js}'],
  theme: {
    colors: {
      '1': '#5A5B5D',
      '2': '#38393B',
      '3': '#242526',
      '4': '#1A1B1C',
      '5': '#111212',
    },
    fontFamily: {
      serif: ['Georgia', 'serif'],
      sans: ['Arial', 'sans'],
      monospace: ['Courier New', 'monospace'],
      cursive: ['Dancing Script', 'cursive'],
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {
      spacing: {
        '8xl': '96rem',
        '9xl': '128rem',
      },
      borderRadius: {
        '4xl': '2rem',
      },
      plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
      ],
    }
  },
}




// @type {import('tailwindcss').Config} 

// module.exports = {
//   content: ['.src/**/*.{html,js}'],
//   theme: {
//     extend: {
//       fontFamily: {
//         serif: ['Georgia', 'serif'],
//         sans: ['Arial', 'sans'],
//         monospace: ['Courier New', 'monospace'],
//         cursive: ['Dancing Script', 'cursive'],
//       },
//     },
//     colors: {
//       gray: {

//       },
//     },
//   },
//   variants: {},
//   plugins: [
//     require('@tailwindcss/forms'),
//     require('@tailwindcss/typography'),
//   ],
// };


// purge: [
//   './templates/**/*.html',
// ],