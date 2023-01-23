$("#id_order").change(function () {
  $(".form").submit();
});

$(".toggle-star").click(function () {
  id = $(this).attr("value");
  temp = $(this);
  $.ajax({
    type: "POST",
    url: "/toggle-star",
    data: { pk: id },
    datatype: "json",

    success: function (result) {
      temp.toggleClass("fill");
    },
    error: function (e) {
      console.log(e.status);
    },
  });
});

$(".plus").click(function () {
  id = $(this).attr("value");
  temp = $(this).next();
  $.ajax({
    type: "POST",
    url: "/calc-interest",
    data: { pk: id, option: 1 },
    datatype: "json",

    success: function (result) {
      temp.text(result.interest);
    },
    error: function (e) {
      console.log(e.status);
    },
  });
});

$(".minus").click(function () {
  id = $(this).attr("value");
  temp = $(this).prev();
  $.ajax({
    type: "POST",
    url: "/calc-interest",
    data: { pk: id, option: -1 },
    datatype: "json",

    success: function (result) {
      temp.text(result.interest);
    },
    error: function (e) {
      console.log(e.status);
    },
  });
});

//Ajax crsf 토큰 문제 해결 코드
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

var csrftoken = getCookie("csrftoken");

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}
$.ajaxSetup({
  beforeSend: function (xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  },
});
