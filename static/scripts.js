console.log('Script carregado');

let carouselIndex = 0;
showCarousel();

function showCarousel() {
    const slides = document.querySelectorAll('.carousel-item');
    
    
    slides.forEach(slide => {
        slide.style.display = 'none';
    });

    
    carouselIndex++;
    
    
    if (carouselIndex > slides.length) {
        carouselIndex = 1;
    }

    
    slides[carouselIndex - 1].style.display = 'block';

    
    setTimeout(showCarousel, 3000);
}

<script src="{{ url_for('static', filename='js/scripts.js') }}"></script>
