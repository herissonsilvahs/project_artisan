let gulp = require('gulp');
let sass = require('gulp-sass');
 
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
 
 gulp.task('default', ['compile', 'watch']);
 