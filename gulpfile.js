let gulp = require('gulp');
let sass = require('gulp-sass');
let autoprefixer = require('gulp-autoprefixer');
 
 //Compile task
 gulp.task('compile', function () {
     gulp.src('core/static/sass/appp.scss')
         .pipe(sass().on('error', sass.logError))
         .pipe(gulp.dest('core/static/css/'))
 });
 
 //Watch task
 gulp.task('watch', function () {
     gulp.watch('core/static/sass/*.scss', ['compile']);
     // gulp.watch('core/static/scripts/*.js', ['scripts']);
 });

 //Autoprefixer task
gulp.task('auto-prefixer', function () {
   gulp.src('core/static/css/appp.css')
       .pipe(autoprefixer({
           browsers: ['defaults'],
       }))
       .pipe(gulp.dest('core/static/css/'))
});
 
 gulp.task('default', ['compile', 'watch']);
 