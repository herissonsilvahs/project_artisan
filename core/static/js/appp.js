function menuAnim() {
    TweenLite.to('.menu', 1 , {transform: 'scaleY(1)', ease: Power3.easeOut});
    TweenLite.to('.menu__bg', 1 , {css: {transform: 'scaleY(1)', ease: Power3.easeOut}, delay: 0.2});
    TweenMax.staggerTo('.menu__item', 0.5, {css:{ transform: 'translateX(5px)', opacity: 1}, delay: 0.5}, 0.1)
}

function menuIconAnim() {
    TweenMax.staggerTo('.menu-btn__rect:not(.menu-btn__rect--diag)', 0.2, { transform: 'translateX(60px)', opacity: 0, ease: Power2.easeIn}, 0.1);
    TweenMax.to('.menu-btn__rect--diag', 0.5, {css: { opacity: 1, ease: Power2.easeIn}, delay: 0.6}, 0.5)

}

$('.menu-btn').click(function () {
    menuIconAnim();
    menuAnim();
})


//todo: verify if timeline is neccessary