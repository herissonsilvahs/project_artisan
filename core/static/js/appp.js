function menuAnim() {
    let tl = new TimelineLite();

    tl.to('.menu', 1 , {transform: 'scaleY(1)', ease: Power3.easeOut});
    tl.to('.menu__bg', 1 , {transform: 'scaleY(1)', ease: Power3.easeOut}, "-=0.6");
    tl.staggerTo('.menu__item', 0.5, { transform: 'translateX(5px)', opacity: 1}, 0.2 , 0.5)
}

function menuIconAnim() {
    let tl = new TimelineLite();

    tl.staggerTo('.menu-btn__rect:not(.menu-btn__rect--diag)', 0.2, { transform: 'translateX(60px)', opacity: 0, ease: Power2.easeIn}, 0.1);
    tl.to('.menu-btn__rect--diag', 0.5, { onComplete: () => {
        $('.menu-btn__rect--diag:nth-child(4)').css({'transform': 'rotate(45deg) scaleX(1)', 'border-radius': '10px'})
        $('.menu-btn__rect--diag:nth-child(5)').css({'transform': 'rotate(-45deg) scaleX(1)', 'border-radius': '10px'})
    }}, "-=0.4");
}

$('.menu-btn').click(function () {
    menuIconAnim();
    menuAnim();
});