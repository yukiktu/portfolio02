$(function() {
  $('#question_form').submit(function(){
    event.preventDefault();

    now = new Date();
    timestamp = now.toLocaleString();

    question = $('#question').val();
    if(question == ''){
      return;
    }
    message(question, timestamp, 'guest');
    $.ajax({
      type : 'POST',
      url : '/api/talk/',
      datatype : "JSON",
      data : JSON.stringify({
        'question' : question
      }),
      success : function(data) {
        message(data.answer, data.timestamp, 'ai');
      }
    });

    $('#question').val("");

    return false;
  });
});

function message(msg, timestamp, who) {
  var box = null;
  if(who == 'ai'){
    box = '<div class="ai uk-grid-small uk-flex-bottom uk-flex-left" uk-grid><div class="uk-width-auto"><img class="uk-border-circle" width="32" height="32" src="/static/images/robot.jpeg"></div><div class="uk-width-auto"><div class="uk-card uk-card-body uk-card-small uk-card-default uk-border-rounded"><p class="uk-margin-remove">' + msg + '<p class="uk-text-small">' + timestamp + '</p></div></div></div>';
  } else if(who == 'guest'){
    box = '<div class="me uk-grid-small uk-flex-bottom uk-flex-right uk-text-right" uk-grid><div class="uk-width-auto"><div class="uk-card uk-card-body uk-card-small uk-card-primary uk-border-rounded"><p class="uk-margin-remove message">' + msg + '<p class="uk-text-small">' + timestamp + '</p></p></div></div></div>';
  }

  $('#talk').append(box);
  talkboxScroll();
}

function talkboxScroll(){
  $('#talkbox').animate({ scrollTop: $('#talkbox')[0].scrollHeight});
}
