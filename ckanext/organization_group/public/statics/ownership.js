$(document).ready(function(){
    $('select.org_dropdown').select2();
    $('select.group_dropdown').select2();
    $('#groups_dropdown_box_1').show();
    $('#ownership-form').submit(function(e){
        $('#org_group_error').hide();
        $('.org_dropdown').css('border', '');
        let org = $('#org_dropdown').find(':selected').val();
        if(org == '0'){
            e.preventDefault();
            $('#org_group_error').show();
            $('.org_dropdown').css('border', '2px solid red');
        }      
    });
});