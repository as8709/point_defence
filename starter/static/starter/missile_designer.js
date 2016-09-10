$(document).ready(function(){
    /*If the user clicks on the new design button
    hide the default message if it is showing
    Show the design form if it is hidden
    If there is a current design then prompt the user to save
    */
    $("#new_design").click(function(){
        $("#default").hide();
        //TODO check for unsaved designs
        $("#design_form").show().prop("design", "unsaved").trigger("reset");

    });


    $("#design_form").on('submit', function(event){
        event.preventDefault();
        //get the form
        if (this.design === "unsaved") {
            //brand new design
            create_design(this);
        } else {
            //updating an existing design
        }
    });

    //User has selected an existing design
    apply_side_button_cb();



});

function apply_side_button_cb(){
     //User has selected an existing design
    $(".side-button").click(function(){
        $("#default").hide();
        //TODO check for unsaved designs before we overwrite the design
        $("#design_form").show().prop("design", this.id);
        read_design_from_db(this.id);
    });

}

function create_design(form){
    //extract the input data for every field in the form
    var data_obj = {};
    $(form).find("input").each(function(index){
            data_obj[this.id] = this.value;
    });
    $.ajax({
        url : "create_missile_design/",
        type : "POST",
        data : data_obj,

        // handle a successful response
        success : function(json) {
            $('#side_bar').prepend("<button class=\"btn side-button\" type=\"button\" id=" + json.id + ">" + json.name + "</button>");
            $("#design_form").prop("design", json.id);
            apply_side_button_cb();

        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

function read_design_from_db(design_id){
    $.ajax({
        url : "get_missile_design/",
        type : "GET",
        data : {"design_id" : design_id},

        // handle a successful response
        success : function(json) {
            //read the response and fill in the fields on the design_form
            fields = json[0].fields;
            $("#design_form").find("input").each(function(index){
                if(this.id !== ""){
                    //ignore the special csrf field
                    this.value = fields[this.id.slice(3)];
                }
            });
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
}

$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});