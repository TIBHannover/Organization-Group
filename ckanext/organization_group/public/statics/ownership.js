$(document).ready(function(){
    $('select.org_dropdown').select2();
    $('#ownership-form').submit(function(e){
        $('#next-step-loadin-animation').css('display', 'inline-block');
        $('#org_group_error').hide();
        $('.org_dropdown').css('border', '');
        let org = $('#org_dropdown').find(':selected').val();
        if(org == '0'){
            $('#next-step-loadin-animation').css('display', 'none');
            e.preventDefault();
            $('#org_group_error').show();
            $('.org_dropdown').css('border', '2px solid red');
        }      
    });

});