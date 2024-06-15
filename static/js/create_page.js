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

var selectedoption = {
  first: null,
  second: null,
  third: null,
  imageOption: null,
  audioOption: null,
  dalle: null,
  audio: null
};

$(document).ready(function(){
  // 이미지 클릭 시 이벤트 처리
  $('.select-image_1').click(function() {
      var imgSrc = $(this).attr('src');
      var title = $(this).next('.select-title_1').text();

      $('#first').attr('src', imgSrc);
      $('.class-title_1').text(title);
      selectedoption.first = {title};
  });

  $('.select-image_2').click(function() {
    var imgSrc = $(this).attr('src');
    var title = $(this).next('.select-title_2').text();

    $('#second').attr('src', imgSrc);
    $('.class-title_2').text(title);
    selectedoption.second = {title};
  });

  $('.select-image_3').click(function() {
    var imgSrc = $(this).attr('src');
    var title = $(this).next('.select-title_3').text();

    $('#third').attr('src', imgSrc);
    $('.class-title_3').text(title);
    selectedoption.third = {title};
  });

  // 제목 클릭 시 이벤트 처리
  $('.select-title_1').click(function() {
      var imgSrc = $(this).prev().attr('src');
      var title = $(this).text();

      $('#first').attr('src', imgSrc);
      $('.class-title_1').text(title);
      selectedoption.first = {title};
  });

  $('.select-title_2').click(function() {
    var imgSrc = $(this).prev().attr('src');
    var title = $(this).text();

    $('#second').attr('src', imgSrc);
    $('.class-title_2').text(title);
    selectedoption.second = {title};
    });

  $('.select-title_3').click(function() {
    var imgSrc = $(this).prev().attr('src');
    var title = $(this).text();

    $('#third').attr('src', imgSrc);
    $('.class-title_3').text(title);
    selectedoption.third = {title};
    });
  });

  // 모달창에서 선택한 옵션 저장
  $('input[name="dalle"]').change(function() {
    if ($(this).val() === 'add-img') {
      selectedoption.imageOption = 'DALL-E 삽화 추가';
    } else if ($(this).val() === 'null') {
      selectedoption.imageOption = null;
    } else {
      selectedoption.imageOption = null;
    }
    selectedoption.dalle = $(this).val();
  });
  
  $('input[name="audio"]').change(function() {
    if ($(this).val() === 'audio-base') {
      selectedoption.audioOption = '기본 목소리';
    } else if ($(this).val() === 'audio-fem') {
      selectedoption.audioOption = '내 목소리';
    } else if ($(this).val() === 'null') {
      selectedoption.audioOption = null;
    } else {
      selectedoption.audioOption = null;
    }
    selectedoption.audio = $(this).val();
  });
  

  $('.create-btn').click(async function() {
    try {
      const response = await sendCreateInfo();
      console.log('Character info sent successfully:', response);
  
      await generateText(response.folder_path); // 텍스트 생성
      await generateImage(response.folder_path); // 이미지 생성
      await generateAudio(response.folder_path); // 음성 생성 (필요시)
      window.location.href = '/home/dynamic_fairy_list';
      
    } catch (error) {
      console.log('Error:', error);
    }
  });
  
  function sendCreateInfo() {
    return new Promise((resolve, reject) => {
      $.ajax({
        url: '/home/api/sendcreateInfo',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify(selectedoption),
        success: resolve,
        error: reject
      });
    });
  }
  
  function generateText(folderPath) {
    return new Promise((resolve, reject) => {
      $.ajax({
        url: '/home/api/generateText',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
          folder_path: folderPath,
          first: selectedoption.first ? selectedoption.first : '',
          second: selectedoption.second ? selectedoption.second : '',
          third: selectedoption.third ? selectedoption.third : ''
        }),
        success: resolve,
        error: reject
      });
    }).then(response => {
      console.log('Text generated successfully:', response);
    }).catch(error => {
      console.log('Error generating text:', error);
    });
  }
  
  function generateImage(folderPath) {
    return new Promise((resolve, reject) => {
      $.ajax({
        url: '/home/api/generateImage',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
          folder_path: folderPath
        }),
        success: resolve,
        error: reject
      });
    }).then(response => {
      console.log('Images generated successfully:', response);
    }).catch(error => {
      console.log('Error generating images:', error);
    });
  }

  function generateAudio(folderPath) {
    return new Promise((resolve, reject) => {
      $.ajax({
        url: '/home/api/generateAudio',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
          folder_path: folderPath,
          audioOption: selectedoption.audioOption ? selectedoption.audioOption : ''
        }),
        success: resolve,
        error: reject
      });
    }).then(response => {
      console.log('Audio generated successfully:', response);
    }).catch(error => {
      console.log('Error generating audio:', error);
    });
  }

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

const modal = document.querySelector('.modal');
const modalOpen = document.querySelector('.modal-btn');
const modalClose = document.querySelector('.close-btn');

//열기 버튼을 눌렀을 때 모달팝업이 열림
modalOpen.addEventListener('click',function(){
    //'on' class 추가
  modal.classList.add('on');
});
//닫기 버튼을 눌렀을 때 모달팝업이 닫힘
modalClose.addEventListener('click',function(){
    //'on' class 제거
  modal.classList.remove('on');
});