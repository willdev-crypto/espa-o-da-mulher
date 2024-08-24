console.log('Script carregado');

let carouselIndex = 0;
showCarousel();

function showCarousel() {
    let slides = document.querySelectorAll('.carousel-item');
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = 'none';
    }
    carouselIndex++;
    if (carouselIndex > slides.length) {
        carouselIndex = 1;
    }
    slides[carouselIndex - 1].style.display = 'block';
    setTimeout(showCarousel, 3000); // Troca de imagem a cada 3 segundos
}
