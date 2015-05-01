$(document).ready(function() {

    // show pam widget and hide no-js message
    $('#pam-no-js').css('display', 'none');
    $('#pam-widget').css('display', 'block');

    // some variables
    var image_id = $('#pam-image-id');  // hidden form field
    var cells = $('#pam-widget ul li');  // all the pam cells
    var load_more = $('#pam-load-more');  // load more link
    var submit = $('#pam-submit');  // form submission button

    // listener for load more
    load_more.click(function() {
        window.location.reload();
        return false;
    });

    // listener for submit button
    // submit.click(function() {
    //     if (image_id.attr('value') == '') {
    //         alert("Touch how you feel right now\n(pick an image or load new images)");
    //         return false;
    //     }
    // });

    // on-click listeners for each pam cell
    cells.click(function() {
        // set all other cells to normal
        cells.each(function() {
            $(this).css('border', 'none');
            $(this).css('width', '80px');
            $(this).css('height', '80px');
            img = $(this).find('img');
            img.css('margin', '0');
        });

        var colourCloud=0;
        // change this cell's border color
        if($(this).attr('id')<4){
            $(this).css('border', '3px solid #8B0000');
            colourCloud = 1;
        }
        else if($(this).attr('id')<7){
            $(this).css('border', '3px solid #FF0000');
            colourCloud = 1;
        }
        else if($(this).attr('id')<10){
            $(this).css('border', '3px solid #FF6600');
            colourCloud = 3;
        }
        else if($(this).attr('id')<13){
            $(this).css('border', '3px solid #FFFF00');
            colourCloud = 2;
        }
        else if($(this).attr('id')<16){
            $(this).css('border', '3px solid #8B0000');
            colourCloud = 1;
        }
        else if($(this).attr('id')<19){
            $(this).css('border', '3px solid #FF0000');
            colourCloud = 1;
        }
        else if($(this).attr('id')<22){
            $(this).css('border', '3px solid #FFFF00');
            colourCloud = 2;
        }
        else if($(this).attr('id')<25){
            $(this).css('border', '3px solid #33FF33');
            colourCloud = 4;
        }
        else if($(this).attr('id')<28){
            $(this).css('border', '3px solid #474747');
            colourCloud = 9;
        }
        else if($(this).attr('id')<31){
            $(this).css('border', '3px solid #999999');
            colourCloud = 9;
        }
        else if($(this).attr('id')<34){
            $(this).css('border', '3px solid #19E0FF');
            colourCloud = 7;
        }
        else if($(this).attr('id')<37){
            $(this).css('border', '3px solid #0000FF');
            colourCloud = 6;
        }
        else if($(this).attr('id')<40){
            $(this).css('border', '3px solid #999999');
            colourCloud = 9;
        }
        else if($(this).attr('id')<43){
            $(this).css('border', '3px solid #7D26CD');
            colourCloud = 8;
        }
        else if($(this).attr('id')<46){
            $(this).css('border', '3px solid #7D26CD');
            colourCloud = 8;
        }
        else {
            $(this).css('border', '3px solid #40E0D0');
            colourCloud = 5;
        }



        if(colourCloud!=0){
        $(this).css('width', '74px');
        $(this).css('height', '74px');
        img = $(this).find('img');
        img.css('margin', '-3px');
        image_id.attr('value', $(this).attr('id'));

        document.getElementById('pam-form').submit();
        // window.location.replace("http://localhost:8000/self_report.php");


        //$.post("http://128.253.3.144/"+colourCloud).always(function(){ 
          // Handle error here
          //document.getElementById('pam-form').submit();
          
        //});
    
    }
        // update the hidden form field
        

                // return xmlHttp.responseText;
            
        
        // document.getElementById('pam-form').submit();

    });

});
