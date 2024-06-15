$(document).ready(function() {
    function transformNext(event) {
        const slideNext = event.target;

        const classList = slideNext.parentElement.parentElement.nextElementSibling;
        let activeLi = parseInt(classList.getAttribute('data-position'));
        const liList = classList.getElementsByTagName('li');
        const maxPosition = -(liList.length - Math.floor(classList.clientWidth / 380)) * 380;

        if (activeLi > maxPosition) {
            activeLi = Math.max(activeLi - 380, maxPosition);

            classList.style.transition = 'transform 1s';
            classList.style.transform = 'translateX(' + String(activeLi) + 'px)';
            classList.setAttribute('data-position', activeLi);
        }
    }

    function transformPrev(event) {
        const slidePrev = event.target;

        const classList = slidePrev.parentElement.parentElement.nextElementSibling;
        let activeLi = parseInt(classList.getAttribute('data-position'));

        if (activeLi < 0) {
            activeLi = Math.min(activeLi + 380, 0);

            classList.style.transition = 'transform 1s';
            classList.style.transform = 'translateX(' + String(activeLi) + 'px)';
            classList.setAttribute('data-position', activeLi);
        }
    }

    const slidePrevList = document.getElementsByClassName('slide-prev');
    const slideNextList = document.getElementsByClassName('slide-next');

    for (let i = 0; i < slidePrevList.length; i++) {
        slidePrevList[i].addEventListener('click', transformPrev);
    }

    for (let i = 0; i < slideNextList.length; i++) {
        slideNextList[i].addEventListener('click', transformNext);
    }
});
