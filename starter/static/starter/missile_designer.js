$(document).ready(function(){
    /*If the user clicks on the new design button
    hide the default message if it is showing
    Show the design form if it is hidden
    If there is a current design then prompt the user to save
    */
    $("#new_design").click(function(){
        $("#default").hide();
        //TODO check for unsaved designs
        $("#design_form").show().prop("design", "unsaved");

    });


    $("#design_form").on('submit', function(event){
        console.log("Submmit");
        event.preventDefault();
        //get the form
        if (this.design === "unsaved") {
            //brand new design
            create_design(this);
        } else {
            //updating an existing design
        }
    });



});

function create_design(form){
    console.log("creating design");
    //extract the input data for every field in the form
    var data_obj = {};
    $(form).find("input").each(function(index){
        if(this.type == "checkbox") {
            data_obj[this.id] = this.checked;
        }
        else{
            data_obj[this.id] = this.value;
        }

    });
    console.log(data_obj);
    $.ajax({
        url : "create_missile_design/",
        type : "POST",
        data : data_obj,

        // handle a successful response
        success : function(json) {
           //don't need to do anything
           console.log("Added design");
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