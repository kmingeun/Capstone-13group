$(function(){
    $('#slider-div').slick({
        slide: 'div',        
        infinite : true,    
        slidesToShow : 4,        
        slidesToScroll : 4,       
        rows: 2,
        speed : 100,    
        arrows : true,        
        dots : true,        
        pauseOnHover : true,        
        vertical : false,        
        prevArrow : '<i class="fa-solid fa-chevron-left button_left"></i>',  
        nextArrow : '<i class="fa-solid fa-chevron-right button_right"></i>',    
        dotsClass : "slick-dots",     
        draggable : true,     
  
    });
  })
  
  $(document).ready(function(){
    // 이미지 클릭 시 이벤트 처리
    $('.select-image_1').click(function() {
        var imgSrc = $(this).attr('src');
        var title = $(this).next('.select-title_1').text();
  
        $('#first').attr('src', imgSrc);
        $('.class-title_1').text(title);
    });
  
    $('.select-image_2').click(function() {
      var imgSrc = $(this).attr('src');
      var title = $(this).next('.select-title_2').text();
  
      $('#second').attr('src', imgSrc);
      $('.class-title_2').text(title);
    });
  
    $('.select-image_3').click(function() {
      var imgSrc = $(this).attr('src');
      var title = $(this).next('.select-title_3').text();
  
      $('#third').attr('src', imgSrc);
      $('.class-title_3').text(title);
    });
  
    // 제목 클릭 시 이벤트 처리
    $('.select-title_1').click(function() {
        var imgSrc = $(this).prev().attr('src');
        var title = $(this).text();
  
        $('#first').attr('src', imgSrc);
        $('.class-title_1').text(title);
    });
  
    $('.select-title_2').click(function() {
      var imgSrc = $(this).prev().attr('src');
      var title = $(this).text();
  
      $('#second').attr('src', imgSrc);
      $('.class-title_2').text(title);
      });
  
  $('.select-title_3').click(function() {
    var imgSrc = $(this).prev().attr('src');
    var title = $(this).text();
  
    $('#third').attr('src', imgSrc);
    $('.class-title_3').text(title);
    });
  });
  