$(document).ready(function(){
    $("#SlideDown h4").hide();
    $("#fadeIn h4").hide();
    $("#Click button").click(function(){
        $("#Click p").css ("color", "red");
    })
    $("#hide").click(function(){
        $("#HideShow p").hide ();
    })
    $("#show").click(function(){
        $("#HideShow p").show ();
    })
    $("#Toggle button").click(function(){
        $("#Toggle p").toggle('slow');
    })
    $("#SlideDown button").click(function(){
        $("#SlideDown h4").slideDown('slow');
    });
    $("#SlideUp button").click(function(){
        $("#SlideUp h4").slideUp('slow');
    })
    $("#slideToggle button").click(function(){
        $("#slideToggle p").slideToggle("slow");
    })
    $("#fadeIn button").click(function(){
        $("#fadeIn h4").fadeIn("slow");
    })
    $("#fadeOut button").click(function(){
        $("#fadeOut p").fadeOut("slow");
    })
    $("#addClass button").click(function(){
        $("#addClass p").addClass("blue");
    })
    $("#before button").click(function(){
        $("#before h4").before("<b>Told</b>");
    })
    $("#after button").click(function(){
        $("#after p").after("aand this shows up!");
    })
    $("#append button").click(function(){
        $("#append p").append(" so that this text is visible");
    })
    $(".html button").click(function(){
        $(".html p").html("Click the button and <b>I</b> will change!");
    })
    $("#attr button").click(function(){
        $("#attr img").attr ("title", "red hat");
    })
    $("#val button").click(function(){
        $("#computer").val ("PC");
    })
    $("#text button").click(function(){
        $("#text p").text ("This is your new paragraph!");
    })
    $("#data button").click(function(){
        $("span").data ("shoe", {USA: 11, EUR: 42});
        $("span:first").text($("span").data ("shoe").USA);
        $("span:last").text($("span").data ("shoe").EUR);
    })
})