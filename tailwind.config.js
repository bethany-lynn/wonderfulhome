module.exports = {
    purge: [
        './templates/**/*.html',
    ],
    theme: {
        extend: {},
    },
    variants: {},
    plugins: [],
    extend: {
        theme: {
            transitionProperty: {
                'opacity': 'opacity',
            },
            transitionDuration: {
                '700': '700ms',
                '1000': '1000ms', 
            },
            transitionTimingFunction: {
                'ease-in-out': 'ease-in-out',
            },
        },
    },
};
