// Initialize modules
// Importing specific gulp API functions lets us write them below as series() instead of gulp.series()
const { src, dest, watch, series, parallel } = require('gulp');
// Importing all the Gulp-related packages we want to use
const sourcemaps = require('gulp-sourcemaps');
const sass = require('gulp-sass');
const concat = require('gulp-concat');
const uglify = require('gulp-uglify');
const postcss = require('gulp-postcss');
const autoprefixer = require('autoprefixer');
const cssnano = require('cssnano');

// File paths
const files = { 
    scssPath: 'src/scss/**/*.scss',
    jsPath: 'src/js/**/*.js',
    scssPathAr: 'src/arscss/**/*.scss',
}

// Sass task: compiles the style.scss file into style.css
function scssTask(){    
    return src(files.scssPath)
        .pipe(sourcemaps.init()) // initialize sourcemaps first
        .pipe(sass()) // compile SCSS to CSS
        .pipe(postcss([ autoprefixer(), cssnano() ])) // PostCSS plugins
        .pipe(sourcemaps.write('.')) // write sourcemaps file in current directory
        .pipe(dest('static/css')
    ); // put final CSS in dist folder
}

 

// JS task: concatenates and uglifies JS files to script.js
function jsTask(){
    return src([

            'src/js/bootstrap.min.js',
            'src/js/jQuery3.6.min.js',
            'src/js/jQuery-migrate.min.js',
            'src/js/jQuery-validate.min.js',
            'src/js/jQuery-ui.min.js',
            'src/js/select2.min.js',
            'src/js/intl-tel-input.min.js',
            'src/js/fontawesome.min.js',
            'src/js/custom.js'
             //,'!' + 'includes/js/jquery.min.js', // to exclude any specific files
        ])
        .pipe(concat('all.js'))
        .pipe(uglify())
        .pipe(dest('static/js')
    );
}

 

// Watch task: watch SCSS and JS files for changes
// If any change, run scss and js tasks simultaneously
// function watchTask(){
//     watch([files.scssPath, files.jsPath], 
//         parallel(scssTask, jsTask));    
// }
function watchTask(){
    watch([files.scssPath], 
        parallel(scssTask));    
}

// Export the default Gulp task so it can be run
// Runs the scss and js tasks simultaneously
// then runs cacheBust, then watch task
exports.default = series(
    parallel(scssTask, jsTask), 
    watchTask
);